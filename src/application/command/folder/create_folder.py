"""Create folder command handler"""

__author__ = 'infast1k'

from dataclasses import dataclass
from uuid import UUID

from application.command.base.command import BaseCommand, BaseCommandHandler
from application.command.folder.exceptions import FolderAlreadyExistsException

from domain.folder.entity import Folder
from domain.folder.repository import BaseFolderRepository
from domain.folder.value_object import Title


@dataclass(frozen=True)
class CreateFolderCommand(BaseCommand):
    """Command for create new folder"""

    title: str
    parent_id: UUID | None


class CreateFolderCommandHandler(BaseCommandHandler[CreateFolderCommand, Folder]):
    """Handler for processing folder creation"""

    def __init__(self, folder_repository: BaseFolderRepository) -> None:
        """Handler initialization"""
        self._folder_repository: BaseFolderRepository = folder_repository

    async def execute(self, command: CreateFolderCommand) -> Folder:
        """Execute folder creation"""
        title = Title(command.title)
        folder = Folder(title, command.parent_id)

        is_already_exists = await self._folder_repository.folder_already_exists(folder)
        if is_already_exists:
            raise FolderAlreadyExistsException(folder_name=title.value)

        await self._folder_repository.add_folder(folder)

        return folder
