# Standard Library imports
# ----------------------------
from typing import List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class And(BaseOperator):
    """Logical AND operator"""

    __symbol__ = "$and"

    right: List[Expression]

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
