"""Base entity"""

__author__ = 'infast1k'


from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class BaseEntity:
    """Base entity"""

    oid: UUID = field(kw_only=True, default_factory=uuid4)
    created_at: datetime = field(kw_only=True, default_factory=datetime.now)
    updated_at: datetime = field(kw_only=True, default_factory=datetime.now)
