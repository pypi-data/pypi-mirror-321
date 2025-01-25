# Standard Library imports
# ----------------------------
from abc import abstractmethod
from typing import Any, TypeGuard


from pydantic import BaseModel as PydanticBaseModel

Expression = dict[str, Any]


class BaseModel(PydanticBaseModel):
    """Base class for all models."""

    @property
    @abstractmethod
    def expression(self) -> Expression:
        """Expression abstract property"""

    def to_expression(self) -> Expression | list[Expression]:
        """Converts an instance of a class inheriting from BaseModel to an expression"""

        return self.express(self)

    @classmethod
    def express(cls, obj: Any) -> Expression | list[Expression]:
        """Resolves an expression encapsulated in an object from a class inheriting from BaseModel"""

        return express(obj)


def isbasemodel(instance: Any) -> TypeGuard[BaseModel]:
    """Returns true if instance is an instance of BaseModel"""

    return isinstance(instance, BaseModel)


def express(obj: Any) -> dict | list[dict]:
    """Resolves an expression encapsulated in an object from a class inheriting from BaseModel"""

    if isbasemodel(obj):
        output: Expression | list[Expression] = obj.expression
    elif isinstance(obj, list) and any(map(isbasemodel, obj)):
        output = []
        for element in obj:
            if isinstance(element, BaseModel):
                output.append(element.expression)
            else:
                output.append(element)
    elif isinstance(obj, dict):
        output = {}
        for key, value in obj.items():
            if isinstance(value, BaseModel):
                output[key] = value.expression
            else:
                output[key] = express(value)
    else:
        output = obj

    return output


Abstraction = BaseModel
