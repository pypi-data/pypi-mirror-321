# Standard Library imports
# ----------------------------
from enum import StrEnum, IntEnum
from typing import Any, Union

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Type(BaseOperator):
    """BSON type operator"""

    __symbol__ = "$type"

    left: Any
    right: Union[str, int]  # BSON type string or number

    @property
    def expression(self) -> Expression:
        return {self.left: {self.symbol: self.right}}


class TypeStrEnum(StrEnum):
    """BSON type enum"""

    DOUBLE = "double"
    STRING = "string"
    OBJECT = "object"
    ARRAY = "array"
    BINARY = "binData"
    UNDEFINED = "undefined"  # Deprecated
    OBJECT_ID = "objectId"
    BOOLEAN = "bool"
    DATE = "date"
    NULL = "null"
    REGEX = "regex"
    DBPOINTER = "dbPointer"  # Deprecated
    JAVASCRIPT = "javascript"
    SYMBOL = "symbol"  # Deprecated
    INT32 = "int"
    TIMESTAMP = "timestamp"
    INT64 = "long"
    DECIMAL128 = "decimal"
    MIN_KEY = "minKey"
    MAX_KEY = "maxKey"


class TypeIntEnum(IntEnum):
    """BSON type enum"""

    DOUBLE = 1
    STRING = 2
    OBJECT = 3
    ARRAY = 4
    BINARY = 5
    UNDEFINED = 6  # Deprecated
    OBJECT_ID = 7
    BOOLEAN = 8
    DATE = 9
    NULL = 10
    REGEX = 11
    DBPOINTER = 12  # Deprecated
    JAVASCRIPT = 13
    SYMBOL = 14  # Deprecated
    INT32 = 16
    TIMESTAMP = 17
    INT64 = 18
    DECIMAL128 = 19
    MIN_KEY = -1
    MAX_KEY = 127
