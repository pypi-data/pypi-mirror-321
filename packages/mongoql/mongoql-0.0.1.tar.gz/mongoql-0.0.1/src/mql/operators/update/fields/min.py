# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Min(BaseOperator):
    """Update operator to update field if specified value is less than current value"""

    __symbol__ = "$min"

    left: str  # | list[str]
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
