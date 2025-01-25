# Standard Library imports
# ----------------------------
from typing import Union

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Mul(BaseOperator):
    """Update operator to multiply field values"""

    __symbol__ = "$mul"

    left: str
    right: Union[int, float]

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
