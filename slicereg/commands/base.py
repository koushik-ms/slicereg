from abc import ABC, abstractmethod
from typing import List, Optional

from slicereg.core.atlas import Atlas
from slicereg.core.image import Image
from slicereg.core.section import Section


class BaseImageReader(ABC):

    @abstractmethod
    def read(self, filename: str, resolution: Optional[float]) -> Optional[Image]: ...


class BaseRepo(ABC):

    @abstractmethod
    def get_sections(self) -> List[Section]: ...

    @abstractmethod
    def save_section(self, section: Section): ...

    @abstractmethod
    def get_atlas(self) -> Optional[Atlas]: ...

    @abstractmethod
    def set_atlas(self, atlas: Atlas) -> None: ...
