# Standard Library imports
# ----------------------------
from typing import Dict, Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class ElemMatch(BaseOperator):
    """Array $elemMatch operator - matches documents with array element matching all criteria"""

    __symbol__ = "$elemMatch"

    left: str
    right: Dict[str, Any]  # Query criteria to match against array elements

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
