from fastapi import HTTPException

from src.apps.fabric.parser.base import BaseParser


async def create_parser(backend: str) -> BaseParser:
    if backend == 'default':
        from src.apps.fabric.parser.default_parser import DefaultParser
        return await DefaultParser().setup(backend=backend)
    else:
        HTTPException(status_code=400, detail=f'Not found backend: {backend}')


