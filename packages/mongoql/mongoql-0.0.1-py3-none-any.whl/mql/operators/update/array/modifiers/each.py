# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Each(BaseOperator):
    """Modifier for $push to append multiple values"""

    __symbol__ = "$each"

    right: list[Any]

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
