# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Not(BaseOperator):
    """Logical NOT operator"""

    __symbol__ = "$not"

    right: Any

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
