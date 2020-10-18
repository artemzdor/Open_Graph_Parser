from src.apps.fabric.base import BaseFabric
from fastapi import HTTPException


async def create_fabric(backend: str) -> BaseFabric:
    if backend == 'default':
        from src.apps.fabric.default import FabricDefault
        return await FabricDefault().setup(backend=backend)
    else:
        HTTPException(status_code=400, detail=f'Not found backend: {backend}')


