# Standard Library imports
# ----------------------------
from typing import Any, List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class In(BaseOperator):
    """In operator"""

    __symbol__ = "$in"

    left: Any
    right: List[Any]

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
