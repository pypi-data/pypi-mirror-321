# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Expr(BaseOperator):
    """Expression operator - allows use of aggregation expressions in query"""

    __symbol__ = "$expr"

    right: Any  # Aggregation expression

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
