# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class FilteredPositional(BaseOperator):
    """Update operator to modify array elements that match arrayFilters condition"""

    __symbol__ = "$[identifier]"  # Will be replaced with actual identifier

    left: str
    right: Any
    identifier: str

    @property
    def expression(self) -> Expression:
        symbol = f"$[{self.identifier}]"
        return {f"{self.left}.{symbol}": self.right}
