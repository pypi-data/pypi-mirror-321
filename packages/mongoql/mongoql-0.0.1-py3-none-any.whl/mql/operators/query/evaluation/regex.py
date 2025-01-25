# Standard Library imports
# ----------------------------
from typing import List
from enum import StrEnum


# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class OptionsEnum(StrEnum):
    """Regular expression options"""

    i = "i"  # case insensitive
    m = "m"  # multi line
    x = "x"  # comments
    s = "s"  # dotall
    u = "u"  # unicode


class Regex(BaseOperator):
    """Regular expression operator"""

    __symbol__ = "$regex"

    left: str
    right: str  # regex pattern
    options: List[OptionsEnum] = []

    @property
    def expression(self) -> Expression:
        expr = {self.left: {self.symbol: self.right}}
        if self.options:
            expr[self.left]["$options"] = "".join(
                [option.value for option in self.options]
            )
        return expr
