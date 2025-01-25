# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Gt(BaseOperator):
    """Greater than operator"""

    __symbol__ = "$gt"

    left: Any
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
