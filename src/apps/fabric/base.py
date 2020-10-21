from abc import ABC, abstractmethod

from src.apps.fabric.parser.base import BaseParser


class BaseFabric(ABC):
    _parser: BaseParser

    @abstractmethod
    async def setup(self, backend: str) -> 'BaseFabric':
        pass

    @property
    @abstractmethod
    def parser(self) -> BaseParser:
        pass
