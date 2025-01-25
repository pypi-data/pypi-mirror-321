# Standard Library imports
# ----------------------------
from typing import Union

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Inc(BaseOperator):
    """Update operator to increment field values"""

    __symbol__ = "$inc"

    left: str
    right: Union[int, float]

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
