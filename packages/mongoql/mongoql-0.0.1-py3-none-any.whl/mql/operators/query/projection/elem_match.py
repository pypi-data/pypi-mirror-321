# Standard Library imports
# ----------------------------
from typing import Dict, Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class ElemMatch(BaseOperator):
    """Projection $elemMatch operator - returns first array element matching the specified criteria"""

    __symbol__ = "$elemMatch"

    left: str
    right: Dict[str, Any]  # Query criteria for array elements

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
