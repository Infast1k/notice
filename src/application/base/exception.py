"""Base domain exception"""

__author__ = 'infast1k'

from dataclasses import dataclass

from domain.base.exception import ApplicationException


@dataclass(frozen=True, eq=False)
class LogicException(ApplicationException):
    """Base logic layer exception"""

    @property
    def message(self) -> str:
        """Message of exception"""
        return 'Logic error was occurred'
