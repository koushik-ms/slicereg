from __future__ import annotations

from abc import ABC, abstractmethod

from numpy import ndarray

from slicereg.application.base import BaseSectionRepo
from slicereg.models.section import Section


class BaseRepo(ABC):

    @abstractmethod
    def get_section(self) -> Section: ...


class SelectChannelCommand:

    def __init__(self, repo: BaseSectionRepo, presenter: BasePresenter):
        self._repo = repo
        self._presenter = presenter

    def __call__(self, num: int):
        section = self._repo.sections[0]
        if section is None:
            self._presenter.show_error("No section loaded yet.")
        try:
            image = section.image.channels[num - 1]
            self._presenter.show(channel=num, image=image)
        except IndexError:
            self._presenter.show_error(f"Section doesn't have a Channel {num}.")


class BasePresenter(ABC):

    @abstractmethod
    def show(self, channel: int, image: ndarray): ...

    @abstractmethod
    def show_error(self, msg: str): ...