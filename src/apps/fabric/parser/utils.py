from typing import Union, Optional

from pydantic import BaseModel, HttpUrl, ValidationError

from src.apps.models.open_graph import Profile, VideoMovie, VideoTvShow, VideoEpisode, VideoOther, EnumTypeOG, OpenGraph


class UrlModel(BaseModel):
    url: HttpUrl


def validate_url(url: str) -> bool:
    if url is None:
        return False
    try:
        UrlModel(url=url)
        return True
    except ValidationError:
        return False


def get_profile(content: str) -> Profile:
    if validate_url(content):
        return Profile(url=content)
    return Profile(first_name=content)


def get_video_is_type(open_graph: OpenGraph) -> Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]]:
    result: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = None
    if open_graph.type == EnumTypeOG.video_movie and open_graph.video_movie:
        result = open_graph.video_movie[-1]
    elif open_graph.type == EnumTypeOG.video_episode and open_graph.video_episode:
        result = open_graph.video_episode[-1]
    elif open_graph.type == EnumTypeOG.video_tv_show and open_graph.video_tv_show:
        result = open_graph.video_tv_show[-1]
    elif open_graph.type == EnumTypeOG.video_other and open_graph.video_other:
        result = open_graph.video_other[-1]
    return result
