# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Exists(BaseOperator):
    """Element exists operator"""

    __symbol__ = "$exists"

    left: Any
    right: bool

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
