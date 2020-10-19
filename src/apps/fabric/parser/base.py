from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Callable
from .parser_methods import *

from src.apps.models.open_graph import OpenGraph
from src.apps.models.parsers.tags import TagOR


class BaseParser(ABC):

    map_node_og: Dict[str, Callable[[TagOR, OpenGraph], bool]] = {
        'og:title': og_title,
        'og:determiner': og_determiner,
        'og:description': og_description,
        'og:site_name': og_site_name,
        'og:url': og_url,
        'og:locale': og_locale,
        'og:locale:alternate': og_locale_alternate,
        'og:type': og_type,
        'og:image': og_image,
        'og:image:secure_url': og_image_secure_url,
        'og:image:type': og_image_type,
        'og:image:width': og_image_width,
        'og:image:height': og_image_height,
        'og:image:alt': og_image_alt,
        'og:audio': og_audio,
        'og:audio:secure_url': og_audio_secure_url,
        'og:audio:type': og_audio_type,
        'og:audio:alt': og_audio_alt,
        'og:video': og_video,
        'og:video:secure_url': og_video_secure_url,
        'og:video:type': og_video_type,
        'og:video:width': og_video_width,
        'og:video:height': og_video_height,
        'music:duration': music_duration,
        'music:album': music_album,
        'music:album:disc': music_album_disc,
        'music:album:track': music_album_track,
        'music:musician': music_musician,
        'music:song': music_song,
        'music:song:disc': music_song_disc,
        'music:song:track': music_song_track,
        'music:release_date': music_release_date,
        'music:creator': music_creator,
        'video:actor': video_actor,
        'video:actor:role': video_actor_role,
        'video:director': video_director,
        'video:writer': video_writer,
        'video:duration': video_duration,
        'video:release_date': video_release_date,
        'video:tag': video_tag,
        'video:series': video_series,
        'article:published_time': article_published_time,
        'article:modified_time': article_modified_time,
        'article:expiration_time': article_expiration_time,
        'article:author': article_author,
        'article:section': article_section,
        'article:tag': article_tag,
        'book:author': book_author,
        'book:isbn': book_isbn,
        'book:release_date': book_release_date,
        'book:tag': book_tag,
        'profile:first_name': profile_first_name,
        'profile:last_name': profile_last_name,
        'profile:username': profile_username,
        'profile:gender': profile_gender,
    }

    async def setup(self, backend: str) -> 'BaseParser':
        return self

    @abstractmethod
    async def get_context_url(self, url: str) -> str:
        pass

    @abstractmethod
    def get_list_tags(self, content_site: str) -> Optional[List[TagOR]]:
        pass

