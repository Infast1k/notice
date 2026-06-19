"""Composition exceptions"""

__author__ = 'infast1k'


from dataclasses import dataclass

from application.base.exception import LogicException
from application.command.base.command import BaseCommand


@dataclass(frozen=True, eq=False)
class CommandHandlerNotRegisteredException(LogicException):
    """Command exception if command handler was not found by provided command type"""

    command_type: type[BaseCommand]

    @property
    def message(self) -> str:
        """Message of exception"""
        return f'Command handler was not found by provided command type: "{self.command_type}"'
