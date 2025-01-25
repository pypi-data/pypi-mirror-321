from mql.base import BaseModel


class BaseOperator(BaseModel):
    """Base class for all operators"""

    __symbol__ = ""

    @property
    def symbol(self) -> str:
        """Symbol property"""

        return self.__symbol__
