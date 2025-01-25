# Standard Library imports
# ----------------------------
from typing import List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Mod(BaseOperator):
    """Modulo operator"""

    __symbol__ = "$mod"

    left: str
    right: List[int]  # [divisor, remainder]

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
