# Standard Library imports
# ----------------------------
from typing import Literal

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Unset(BaseOperator):
    """Update operator to remove fields"""

    __symbol__ = "$unset"

    left: str

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: ""}}
