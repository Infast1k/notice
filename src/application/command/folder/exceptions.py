"""Exceptions for folders application layer"""

__author__ = 'infast1k'

from dataclasses import dataclass

from application.base.exception import LogicException


@dataclass(frozen=True, eq=False)
class FolderAlreadyExistsException(LogicException):
    """Exception with create new folder"""

    folder_name: str

    @property
    def message(self) -> str:
        """Message of exception"""
        return f'Message with name "{self.folder_name}" already exists'
