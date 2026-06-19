"""Command mediator abstraction"""

__author__ = 'infast1k'

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from application.command.base.command import CR, CT, BaseCommand, BaseCommandHandler


@dataclass(eq=False)
class BaseCommandMediator(ABC):
    """Base mediator abstraction with common methods"""

    command_map: dict[type[BaseCommand], BaseCommandHandler] = field(
        default_factory=dict,
        kw_only=True,
    )

    @abstractmethod
    def register_command(self, command: type[BaseCommand], command_handler: BaseCommandHandler[CT, CR]) -> None:
        """Register command_handler to command"""
        ...

    @abstractmethod
    def handle_command(self, command: BaseCommand) -> CR:
        """Execute command_handler by provided command"""
        ...
