from typing import Optional, List, Callable

import uvicorn
from pydantic import AnyHttpUrl
from fastapi import FastAPI, APIRouter, Query, Depends

from src.apps.fabric.base import BaseFabric
from src.apps.models.parsers.tags import TagOR
from src.apps.models.open_graph import OpenGraph
from src.apps.fabric.creator import create_fabric
from src.settings.settings import SERVER_HOST, SERVER_PORT


router_cm: APIRouter = APIRouter()


async def get_fabric(backend: Optional[str] = Query(default='default', description='backend парсера')) -> BaseFabric:
    fabric: BaseFabric = await create_fabric(backend=backend)
    return fabric


@router_cm.get(
    path='/get_og',
    response_model=OpenGraph,
    description='Получение OG',
    name='Получение OG'
)
async def get_og(
    url: AnyHttpUrl = Query(default=..., description='Url сайта'),
    fabric: BaseFabric = Depends(get_fabric, use_cache=True)
):
    content_site: str = await fabric.parser.get_context_url(url=str(url))
    tags: List[TagOR] = fabric.parser.get_list_tags(content_site=content_site)
    open_graph: OpenGraph = OpenGraph()

    for tag in tags:
        fun: Optional[Callable[[TagOR, OpenGraph], bool]] = fabric.parser.map_node_og.get(tag.property_name)
        if fun is None:
            continue
        fun(tag, open_graph)

    return open_graph


def get_application() -> FastAPI:
    application: FastAPI = FastAPI(
        title='Open-Graph-Parser',
        debug=True,
        version='1.0.0'
    )

    application.include_router(
        router=router_cm,
        prefix='/api/v1',
        tags=['Open Graph'],
    )

    return application


def main() -> None:
    app: FastAPI = get_application()
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    main()
