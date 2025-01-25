# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Set(BaseOperator):
    """Update operator to set field values"""

    __symbol__ = "$set"

    left: str
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
