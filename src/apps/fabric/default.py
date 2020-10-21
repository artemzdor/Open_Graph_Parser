from src.apps.fabric.base import BaseFabric
from src.apps.fabric.parser.base import BaseParser
from src.apps.fabric.parser.creator import create_parser


class FabricDefault(BaseFabric):
    _parser: BaseParser

    async def setup(self, backend: str) -> 'FabricDefault':
        self._parser = await create_parser(backend=backend)
        return self

    @property
    def parser(self) -> BaseParser:
        return self._parser
