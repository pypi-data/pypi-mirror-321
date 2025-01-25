# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Positional(BaseOperator):
    """Update operator to modify first array element that matches query condition"""

    __symbol__ = "$"

    left: str
    right: Any

    @property
    def expression(self) -> Expression:
        return {f"{self.left}.{self.symbol}": self.right}
