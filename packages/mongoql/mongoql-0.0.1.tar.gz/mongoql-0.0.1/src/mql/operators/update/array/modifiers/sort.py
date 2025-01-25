# Standard Library imports
# ----------------------------
from typing import Union, Dict, Literal

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Sort(BaseOperator):
    """Modifier for $push to sort array elements"""

    __symbol__ = "$sort"

    right: Union[Literal[1, -1], Dict[str, Literal[1, -1]]]

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
