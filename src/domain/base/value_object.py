"""Base value objects"""

__author__ = 'infast1k'


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


ValueType = TypeVar('ValueType', bound=Any)
""" Generic type for base value object """


@dataclass(frozen=True)
class BaseValueObject(Generic[ValueType], ABC):
    """Base value object"""

    value: ValueType

    def __post_init__(self) -> None:
        """post validation after create value"""
        self._validate()

    @abstractmethod
    def _validate(self) -> None:
        """value object validator"""
        ...
