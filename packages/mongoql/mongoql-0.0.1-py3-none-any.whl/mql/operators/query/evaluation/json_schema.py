# Standard Library imports
# ----------------------------
from typing import Dict, Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class JsonSchema(BaseOperator):
    """JSON Schema validation operator"""

    __symbol__ = "$jsonSchema"

    right: Dict[str, Any]  # JSON Schema document

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
