# pylint: disable=C0114
from typing import Any
from ..function_focus import MatchDecider
from ..args import Args


class No(MatchDecider):
    """returns False"""

    def check_valid(self) -> None:
        self.args = Args(matchable=self)
        self.args.validate(self.siblings())
        super().check_valid()

    def _produce_value(self, skip=None) -> None:
        self.value = self.matches(skip=skip)

    def _decide_match(self, skip=None) -> None:
        self.match = False
