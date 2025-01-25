# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Lte(BaseOperator):
    """Less than or equal operator"""

    __symbol__ = "$lte"

    left: Any
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}
