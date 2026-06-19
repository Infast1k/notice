"""Mediator implementation"""

__author__ = 'infast1k'

from dataclasses import dataclass

from application.command.base.command import CR, CT, BaseCommand, BaseCommandHandler

from composition.mediator.command import BaseCommandMediator
from composition.mediator.exception import CommandHandlerNotRegisteredException


@dataclass(eq=False)
class Mediator(BaseCommandMediator):
    """Main mediator"""

    def register_command(self, command: type[BaseCommand], command_handler: BaseCommandHandler[CT, CR]) -> None:
        """Register provided command handler to provided command"""
        self.command_map[command] = command_handler

    async def handle_command(self, command: BaseCommand) -> CR:
        """Find and execute command handler by provided command"""
        command_type = command.__class__
        command_handler = self.command_map.get(command_type)

        if not command_handler:
            raise CommandHandlerNotRegisteredException(command_type)

        return await command_handler.execute(command)
