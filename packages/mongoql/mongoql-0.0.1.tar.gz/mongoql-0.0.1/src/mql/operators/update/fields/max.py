# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Max(BaseOperator):
    """Update operator to update field if specified value is greater than current value"""

    __symbol__ = "$max"

    left: str
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
