from typing import Optional, List

import aiohttp
from bs4 import BeautifulSoup, ResultSet, Tag
from fastapi import HTTPException
from src.apps.fabric.parser.base import BaseParser
from src.apps.models.parsers.tags import TagOR


class DefaultParser(BaseParser):

    async def get_context_url(self, url: str) -> str:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(url)) as resp:
                    if resp.content.total_bytes < 1024 * 1024:
                        markup: str = await resp.text(encoding='utf-8')
                        return markup
                    raise HTTPException(status_code=500, detail='')
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    def get_list_tags(self, content_site: str) -> List[TagOR]:
        soup: Optional[BeautifulSoup] = None
        result: List[TagOR] = list()
        try:
            soup = BeautifulSoup(content_site, 'lxml')
        except Exception as error:
            raise HTTPException(status_code=500, detail=f'{error}')

        result_set: ResultSet = soup.select('html head meta')

        for tag in result_set:
            if isinstance(tag, Tag):
                property_name: Optional[str] = tag.attrs.get('property')
                content: Optional[str] = tag.attrs.get('content')
                source: str = str(tag)
                if property_name and content:
                    tag_or: TagOR = TagOR(property_name=property_name, content=content, source=source)
                    result.append(tag_or)
        return result
