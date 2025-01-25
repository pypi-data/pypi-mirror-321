# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Position(BaseOperator):
    """Modifier for $push to specify the position to insert elements"""

    __symbol__ = "$position"

    right: int

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
