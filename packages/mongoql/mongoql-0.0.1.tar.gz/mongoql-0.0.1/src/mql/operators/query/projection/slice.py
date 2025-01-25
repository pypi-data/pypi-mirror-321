# Standard Library imports
# ----------------------------
from typing import Union, List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Slice(BaseOperator):
    """Projection $slice operator - controls number of array elements to return"""

    __symbol__ = "$slice"

    left: str
    right: Union[int, List[int]]  # Single number or [skip, limit]

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
