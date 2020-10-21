from fastapi import HTTPException

from src.apps.fabric.base import BaseFabric
from src.apps.fabric.default import FabricDefault


async def create_fabric(backend: str) -> BaseFabric:
    if backend == 'default':
        return await FabricDefault().setup(backend=backend)
    HTTPException(status_code=400, detail=f'Not found backend: {backend}')
