from abc import ABC, abstractmethod
from typing import Optional, List

from bs4 import BeautifulSoup

from src.apps.models.parsers.tags import TagOR


class BaseParser(ABC):

    async def setup(self, backend: str) -> 'BaseParser':
        return self

    @abstractmethod
    async def get_context_url(self, url: str) -> str:
        pass

    @abstractmethod
    def get_list_tag_og(self, content_site: str) -> Optional[List[TagOR]]:
        pass

