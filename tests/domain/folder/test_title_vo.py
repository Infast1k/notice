"""Tests for folder title"""

__author__ = 'infast1k'

import pytest

from domain.folder.exception import EmptyTitleException, TitleTooLongException
from domain.folder.value_object import Title


def test_empty_folder_title() -> None:
    """Test empty folder title"""
    with pytest.raises(EmptyTitleException):
        Title('')


def test_too_long_title() -> None:
    """Test too long folder title"""
    with pytest.raises(TitleTooLongException):
        Title('a' * 256)


def test_success_short_title() -> None:
    """Test short folder title"""
    raw_title = 'a'
    title = Title(raw_title)

    assert title.value == raw_title


def test_success_long_title() -> None:
    """Test long folder title"""
    raw_title = 'a' * 255
    title = Title(raw_title)

    assert title.value == raw_title


def test_success_medium_title() -> None:
    """Test medium folder title"""
    raw_title = 'a' * (255 // 2)
    title = Title(raw_title)

    assert title.value == raw_title
