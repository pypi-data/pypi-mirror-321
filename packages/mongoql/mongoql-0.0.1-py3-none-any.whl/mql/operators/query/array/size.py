# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Size(BaseOperator):
    """Array $size operator - matches arrays with specified length"""

    __symbol__ = "$size"

    left: str
    right: int  # Required length of array

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
