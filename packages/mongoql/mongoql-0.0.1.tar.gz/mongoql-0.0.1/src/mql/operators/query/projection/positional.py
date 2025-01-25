# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Positional(BaseOperator):
    """Projection positional $ operator - returns first array element that matches the query"""

    __symbol__ = "$"

    left: str

    @property
    def expression(self) -> Expression:
        return {f"{self.left}.{self.symbol}": 1}
