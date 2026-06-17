"""Base commands objects"""

__author__ = 'infast1k'

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


@dataclass(frozen=True)
class BaseCommand(ABC):
    """Base command"""


CT = TypeVar('CT', bound=BaseCommand)
CR = TypeVar('CR', bound=Any)


class BaseCommandHandler(Generic[CT, CR], ABC):
    """Base command handler"""

    @abstractmethod
    async def execute(self, command: CT) -> CR:
        """Main method for execute command"""
        raise NotImplementedError
