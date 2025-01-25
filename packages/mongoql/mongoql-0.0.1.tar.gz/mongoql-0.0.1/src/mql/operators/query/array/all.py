# Standard Library imports
# ----------------------------
from typing import Any, List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class All(BaseOperator):
    """Array $all operator - matches arrays that contain all specified elements"""

    __symbol__ = "$all"

    left: str
    right: List[Any]  # List of values that must all be present

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
