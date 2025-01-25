# Standard Library imports
# ----------------------------
from typing import str

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Rename(BaseOperator):
    """Update operator to rename fields"""

    __symbol__ = "$rename"

    left: str  # Old field name
    right: str  # New field name

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
