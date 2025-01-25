# Standard Library imports
# ----------------------------
from typing import Union

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Where(BaseOperator):
    """JavaScript evaluation operator"""

    __symbol__ = "$where"

    right: Union[str, callable]  # JavaScript function as string or callable

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
