# Standard Library imports
# ----------------------------
from typing import List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Or(BaseOperator):
    """Logical OR operator"""

    __symbol__ = "$or"

    right: List[Expression]

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
