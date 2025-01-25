# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Push(BaseOperator):
    """Update operator to append values to array"""

    __symbol__ = "$push"

    left: str
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}
