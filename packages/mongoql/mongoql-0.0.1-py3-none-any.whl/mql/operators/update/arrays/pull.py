# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Pull(BaseOperator):
    """Update operator to remove all array elements that match a specified query"""

    __symbol__ = "$pull"

    left: str
    right: Any  # Query condition

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
