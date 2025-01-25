# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Ne(BaseOperator):
    """Not equal operator"""

    __symbol__ = "$ne"

    left: Any
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
