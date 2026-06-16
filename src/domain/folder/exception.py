"""Exceptions for folder domain"""

__author__ = 'infast1k'

from dataclasses import dataclass

from domain.base.exception import ApplicationException


@dataclass(frozen=True, eq=False)
class EmptyTitleException(ApplicationException):
    """Raise exception if folder title is empty"""

    @property
    def message(self) -> str:
        """Message of exception"""
        return 'Folder title cannot be empty'


@dataclass(frozen=True, eq=False)
class TitleTooLongException(ApplicationException):
    """Raise exception if folder title too long"""

    @property
    def message(self) -> str:
        """Message of exception"""
        return 'Folder title too long'
