# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Slice(BaseOperator):
    """Modifier for $push to limit the array size"""

    __symbol__ = "$slice"

    right: int

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
