"""Folder entity"""

__author__ = 'infast1k'

from dataclasses import dataclass, field
from uuid import UUID

from domain.base.entity import BaseEntity
from domain.folder.value_object import Title


@dataclass(eq=False)
class Folder(BaseEntity):
    """Folder entity"""

    title: Title
    parent_oid: UUID | None = field(default=None)
