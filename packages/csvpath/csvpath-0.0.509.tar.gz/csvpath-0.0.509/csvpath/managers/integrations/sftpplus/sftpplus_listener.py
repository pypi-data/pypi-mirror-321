import os
import json
import threading
import paramiko
from tempfile import NamedTemporaryFile
from csvpath import CsvPaths
from csvpath.managers.metadata import Metadata
from csvpath.managers.paths.paths_metadata import PathsMetadata
from csvpath.managers.listener import Listener
from csvpath.util.var_utility import VarUtility
from csvpath.util.metadata_parser import MetadataParser


#
# this class listens for paths events. when it gets one it generates
# a file of instructions and sends them to an SFTPPlus mailbox account.
# a transfer on the landing dir moves the instructions to a holding
# location for future reference: `user`/csvpath_messages/handled
#
# before the move happens a script runs to process the instructions.
# the instructions set up a transfer for the named-paths group's
# expected file arrivals.
#
# that transfer executes a script that loads the files as named-files and
# executes a run of the named-paths on the new named-file. it then moves
# the arrived file to a holding location for process debugging reference.
# the single-source authorative file is at this point in the named-files
# inputs directory, whereever that is configured.
#
class SftpPlusListener(Listener, threading.Thread):
    def __init__(self, *, config=None):
        super().__init__(config)
        self._server = None
        self._port = None
        self._mailbox_user = None
        self._mailbox_password = None
        self._active = False
        self._named_file_name = None
        self._account_name = None
        self._run_method = None
        self.csvpaths = CsvPaths()
        self.result = None
        self.metadata = None
        self.results = None

    def _collect_fields(self) -> None:
        # collect the metadata from comments. we don't have vars so just an
        # empty set there. as we loop through we will overwrite metadata keys
        # if there are dups across the csvpaths. this raises the topic of
        # how to organize data providers/streams in CsvPath. regardless, there
        # are enough ways to organize that imho we don't have to be overly
        # sensitive to the constraint here.
        m = {}
        for p in self.metadata.named_paths:
            MetadataParser(None).collect_metadata(m, p)
        v = {}
        # comments metadata
        self._active = VarUtility.get_bool(m, v, "sftpplus-active")
        self._account_name = VarUtility.get_str(m, v, "sftpplus-account-name")
        self._named_file_name = VarUtility.get_str(m, v, "sftpplus-named-file-name")
        self._run_method = VarUtility.get_str(m, v, "sftpplus-run-method")
        #
        # config.ini stuff:
        #
        # user
        #
        self._mailbox_user = self.csvpaths.config.get(
            section="sftpplus", name="mailbox_user"
        )
        if self._mailbox_user is None:
            raise ValueError("SFTPPlus mailbox username cannot be None")
        if VarUtility.isupper(self._mailbox_user):
            self._mailbox_user = os.getenv(self._mailbox_user)
        #
        # password
        #
        self._mailbox_password = self.csvpaths.config.get(
            section="sftpplus", name="mailbox_password"
        )
        if self._mailbox_password is None:
            raise ValueError("SFTPPlus mailbox password cannot be None")
        if VarUtility.isupper(self._mailbox_password):
            self._mailbox_password = os.getenv(self._mailbox_password)
        #
        # server
        #
        self._server = self.csvpaths.config.get(section="sftpplus", name="server")
        if self._server is None:
            raise ValueError("SFTPPlus server cannot be None")
        if VarUtility.isupper(self._server):
            self._server = os.getenv(self._server)
        #
        # port
        #
        self._port = self.csvpaths.config.get(section="sftpplus", name="port")
        if self._port is None:
            raise ValueError("SFTPPlus port cannot be None")
        if VarUtility.isupper(self._port):
            self._port = os.getenv(self._port)

    @property
    def run_method(self) -> str:
        if self._run_method is None or self._method not in [
            "collect_paths",
            "fast_forward_paths",
            "collect_by_line",
            "fast_forward_by_line",
        ]:
            self.csvpaths.logger.warning(
                "No acceptable sftpplus-run-method found by SftpSender for {self.metadata.named_paths_name}: {self._method}. Defaulting to collect_paths."
            )
            self._run_method = "collect_paths"
        return self._run_method

    def run(self):
        self.csvpaths.logger.info("Checking for requests to send result files by SFTP")
        self._metadata_update()

    def metadata_update(self, mdata: Metadata) -> None:
        if mdata is None:
            raise ValueError("Metadata cannot be None")
        if not isinstance(mdata, PathsMetadata):
            if self.csvpaths:
                self.csvpaths.logger.warning(
                    "SftpplusListener only listens for paths events. Other event types are ignored."
                )
        self.metadata = mdata
        self.start()

    def _metadata_update(self) -> None:
        self._collect_fields()
        msg = self._create_instructions()
        self._send_message(msg)

    def _send_message(self, msg: dict) -> None:
        #
        # write instructions message into a temp file
        #
        with NamedTemporaryFile(mode="w+t", delete_on_close=False) as file:
            json.dump(msg, file, indent=2)
            file.seek(0)
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                """
                raise Exception(
                    f"SftpPlus list: server: {self._server}, port: {self._port}, user: {self._mailbox_user}, passwd: {self._mailbox_password}"
                )
                """
                client.connect(
                    self._server, self._port, self._mailbox_user, self._mailbox_password
                )
                #
                # create the remote dir, in the messages account, if needed.
                #
                sftp = client.open_sftp()
                try:
                    sftp.stat(self._account_name)
                except FileNotFoundError:
                    sftp.mkdir(self._account_name)
                #
                # land the file at the UUID so that if anything weird we'll only ever
                # interfere with ourselves.
                #
                remote_path = f"{self.metadata.uuid_string}.json"
                self.csvpaths.logger.info("Putting %s to %s", file, remote_path)
                sftp.putfo(file, remote_path)
                sftp.close()
            finally:
                client.close()

    def _create_instructions(self) -> dict:
        #
        # SFTPPLUS TRANSFER SETUP STUFF
        # we are collecting info for the transfer creator class.
        # it will be used to create the message-receiving transfer
        # that handles new file arrivals.
        #
        # most of the information the transer creating code needs comes
        # from its own config.ini.
        #
        msg = {}
        msg["named_paths_name"] = self.metadata.named_paths_name
        msg["account_name"] = self._account_name
        msg["method"] = self._run_method
        #
        # make "description" to "uuid". doesn't matter here
        # that it ends up in the transfer's description field
        #
        msg["uuid"] = f"{self.metadata.uuid_string}"
        msg["named_file_name"] = f"{self._named_file_name}"
        msg["active"] = self._active
        return msg
