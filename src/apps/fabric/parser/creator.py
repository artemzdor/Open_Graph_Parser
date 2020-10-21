from fastapi import HTTPException

from src.apps.fabric.parser.base import BaseParser
from src.apps.fabric.parser.default_parser import DefaultParser


async def create_parser(backend: str) -> BaseParser:
    if backend == 'default':
        return DefaultParser()
    raise HTTPException(status_code=400, detail=f'Not found backend: {backend}')
