"""Value objects for folders"""

__author__ = 'infast1k'


from dataclasses import dataclass

from domain.base.value_object import BaseValueObject
from domain.folder.exception import EmptyTitleException, TitleTooLongException


@dataclass(frozen=True)
class Title(BaseValueObject[str]):
    """Value object for folder title"""

    def _validate(self) -> None:
        """Validate folder title"""
        if not self.value:
            raise EmptyTitleException

        if len(self.value) > 255:
            raise TitleTooLongException
