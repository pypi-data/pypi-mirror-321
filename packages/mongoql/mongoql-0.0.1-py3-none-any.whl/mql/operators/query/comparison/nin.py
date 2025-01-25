# Standard Library imports
# ----------------------------
from typing import Any, List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Nin(BaseOperator):
    """Not in operator"""

    __symbol__ = "$nin"

    left: Any
    right: List[Any]

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
