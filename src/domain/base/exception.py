"""Base domain exception"""

__author__ = 'infast1k'

from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class ApplicationException(Exception):
    """Base domain exception"""

    @property
    def message(self) -> str:
        """Message of exception"""
        return 'Domain error was occurred'
