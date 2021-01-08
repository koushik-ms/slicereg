from typing import Optional

from numpy import ndarray

from src.workflows.load_atlas.load_atlas import BasePresenter as LAPresenter
from src.workflows.load_section.load_section import BasePresenter as BLSPresenter
from src.workflows.move_section.move_section import BasePresenter as MSPresenter
from src.workflows.select_channel.select_channel import BasePresenter as SCPresenter
from src.gui.window import Window


class LoadAtlasPresenter(LAPresenter):

    def __init__(self, win: Window):
        self.win = win

    def show_atlas(self, volume: ndarray, transform: ndarray):
        self.win.volume_view.view_atlas(volume=volume, transform=transform)


class LoadSectionPresenter(BLSPresenter):

    def __init__(self, win: Window):
        self.win = win

    def show_section(self, image: ndarray, transform: Optional[ndarray] = None) -> None:
        self.win.volume_view.view_section(image=image, transform=transform)
        self.win.slice_view.update_slice_image(image=image)


class SelectChannelPresenter(SCPresenter):

    def show_error(self, msg: str) -> None:
        self.win.show_temp_title(msg)

    def update_section_image(self, image: ndarray) -> None:
        self.win.volume_view.update_image(image=image)
        self.win.slice_view.update_slice_image(image=image)

    def __init__(self, win: Window):
        self.win = win


class MoveSectionPresenter(MSPresenter):

    def __init__(self, win: Window):
        self.win = win

    def show_error(self, msg: str) -> None:
        self.win.show_temp_title(msg)

    def update_section_transform(self, transform: ndarray):
        self.win.volume_view.update_transform(transform=transform)
