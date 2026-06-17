"""Base folder repository"""

__author__ = 'infast1k'

from abc import ABC, abstractmethod

from domain.folder.entity import Folder


class BaseFolderRepository(ABC):
    """Folder repository abstraction"""

    @abstractmethod
    async def folder_already_exists(self, folder: Folder) -> bool:
        """Check if folder already exists"""
        ...

    @abstractmethod
    async def add_folder(self, folder: Folder) -> None:
        """Add new folder to storage"""
        ...
