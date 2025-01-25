# Standard Library imports
# ----------------------------
from typing import List, Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class PullAll(BaseOperator):
    """Update operator to remove all matching values from array"""

    __symbol__ = "$pullAll"

    left: str
    right: List[Any]  # List of values to remove

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
