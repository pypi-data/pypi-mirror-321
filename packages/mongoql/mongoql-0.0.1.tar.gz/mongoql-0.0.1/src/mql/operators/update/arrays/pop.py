# Standard Library imports
# ----------------------------
from typing import Literal

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Pop(BaseOperator):
    """Update operator to remove first or last element of array"""

    __symbol__ = "$pop"

    left: str
    right: Literal[-1, 1]  # -1: first element, 1: last element

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
