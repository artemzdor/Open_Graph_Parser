from typing import Union, Optional

from iso8601 import parse_date, ParseError

from src.apps.models.parsers.tags import TagOR
from src.apps.fabric.parser.utils import validate_url, get_profile, get_video_is_type
from src.apps.models.open_graph import OpenGraph, EnumTypeOG, EnumDeterminer, EnumGender, OpenGraphImage
from src.apps.models.open_graph import MusicRadioStation, VideoMovie, VideoEpisode, VideoTvShow, VideoOther
from src.apps.models.open_graph import OpenGraphAudio, OpenGraphVideo, Profile, MusicAlbum, MusicSong, MusicPlayList


INT_MAX: int = 2 ** 31 - 1
INT_MIN: int = - (2 ** 31)

__all__ = ['og_title', 'og_determiner', 'og_description', 'og_site_name', 'og_url', 'og_locale', 'og_locale_alternate',
           'og_type', 'og_image', 'og_image_secure_url', 'og_image_type', 'og_image_width', 'og_image_height',
           'og_image_alt', 'og_audio', 'og_audio_secure_url', 'og_audio_type', 'og_audio_alt', 'og_video',
           'og_video_secure_url', 'og_video_type', 'og_video_width', 'og_video_height', 'music_duration', 'music_album',
           'music_album_disc', 'music_album_track', 'music_musician', 'music_song', 'music_song_disc',
           'music_song_track', 'music_release_date', 'music_creator', 'video_actor', 'video_actor_role',
           'video_director', 'video_writer', 'video_duration', 'video_release_date', 'video_tag', 'video_series',
           'article_published_time', 'article_modified_time', 'article_expiration_time', 'article_author',
           'article_section', 'article_tag', 'book_author', 'book_isbn', 'book_release_date', 'book_tag',
           'profile_first_name', 'profile_last_name', 'profile_username', 'profile_gender']


def og_title(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.title = tag.content
    return True


def og_determiner(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.description = EnumDeterminer(tag.content)
        return True
    except ValueError:
        return False


def og_description(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.description = tag.content
    return True


def og_site_name(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.site_name = tag.content
    return True


def og_url(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.url = tag.content
    return True


def og_locale(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.locale = tag.content
    return True


def og_locale_alternate(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.locale_alternate.append(tag.content)
    return True


def og_type(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.type = EnumTypeOG(tag.content)

        if open_graph.type == EnumTypeOG.music_song:
            open_graph.music_song.append(MusicSong())
        elif open_graph.type == EnumTypeOG.music_album:
            open_graph.music_album.append(MusicAlbum())
        elif open_graph.type == EnumTypeOG.music_playlist:
            open_graph.music_play_list.append(MusicPlayList())
        elif open_graph.type == EnumTypeOG.music_radio_station:
            open_graph.music_radio_station.append(MusicRadioStation())
        elif open_graph.type == EnumTypeOG.video_movie:
            open_graph.video_movie.append(VideoMovie())
        elif open_graph.type == EnumTypeOG.video_episode:
            open_graph.video_episode.append(VideoEpisode())
        elif open_graph.type == EnumTypeOG.video_tv_show:
            open_graph.video_tv_show.append(VideoTvShow())
        elif open_graph.type == EnumTypeOG.video_other:
            open_graph.video_other.append(VideoOther())

        return True
    except ValueError:
        return False


def og_image(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.images.append(OpenGraphImage(url=tag.content))
    return True


def og_image_secure_url(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.images:
        open_graph.images[-1].secure_url = tag.content
        return True
    return False


def og_image_type(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.images:
        open_graph.images[-1].type = tag.content
        return True
    return False


def og_image_width(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.images and tag.content.isdecimal():
        open_graph.images[-1].width = int(tag.content)
        return True
    return False


def og_image_height(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.images and tag.content.isdecimal():
        open_graph.images[-1].height = int(tag.content)
        return True
    return False


def og_image_alt(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.images:
        open_graph.images[-1].alt = tag.content
        return True
    return False


def og_audio(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.audios.append(OpenGraphAudio(url=tag.content))
    return True


def og_audio_secure_url(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.audios:
        open_graph.audios[-1].secure_url = tag.content
        return True
    return False


def og_audio_type(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.audios:
        open_graph.audios[-1].type = tag.content
        return True
    return False


def og_audio_alt(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.audios:
        open_graph.audios[-1].alt = tag.content
        return True
    return False


def og_video(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.videos.append(OpenGraphVideo(url=tag.content))
    return True


def og_video_secure_url(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.videos:
        open_graph.videos[-1].secure_url = tag.content
        return True
    return False


def og_video_type(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.videos:
        open_graph.videos[-1].type = tag.content
        return True
    return False


def og_video_width(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.videos and tag.content.isdigit():
        open_graph.videos[-1].width = tag.content
        return True
    return False


def og_video_height(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.videos and tag.content.isdigit():
        open_graph.videos[-1].height = tag.content
        return True
    return False


def music_duration(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.music_song:
        if tag.content.isdigit() and 1 <= int(tag.content) <= INT_MAX:
            open_graph.music_song[-1].duration = int(tag.content)
            return True
    return False


def music_album(tag: TagOR, open_graph: OpenGraph) -> bool:
    if not open_graph.music_song:
        return False
    if validate_url(tag.content):
        open_graph.music_song[-1].album.append(MusicAlbum(url=tag.content))
    return False


def music_album_disc(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.music_song:
        if tag.content.isdigit() and 1 <= int(tag.content) <= INT_MAX:
            open_graph.music_song[-1].album_disc = int(tag.content)
            return True
    return False


def music_album_track(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.music_song:
        if tag.content.isdigit() and 1 <= int(tag.content) <= INT_MAX:
            open_graph.music_song[-1].album_track = int(tag.content)
            return True
    return False


def music_musician(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.type == EnumTypeOG.music_song and open_graph.music_song:
        open_graph.music_song[-1].musician = get_profile(content=tag.content)
        return True
    if open_graph.type == EnumTypeOG.music_album and open_graph.music_album:
        open_graph.music_album[-1].musician = get_profile(content=tag.content)
        return True
    return False


def music_song(tag: TagOR, open_graph: OpenGraph) -> bool:
    if not validate_url(tag.content):
        return False

    if open_graph.type == EnumTypeOG.music_album and open_graph.music_album:
        open_graph.music_album[-1].song = MusicSong(url=tag.content)
        return True
    if open_graph.type == EnumTypeOG.music_playlist and open_graph.music_play_list:
        open_graph.music_play_list[-1].song = MusicSong(url=tag.content)
        return True

    return False


def music_song_disc(tag: TagOR, open_graph: OpenGraph) -> bool:
    if tag.content.isdigit() and 1 <= int(tag.content) <= INT_MAX:
        if open_graph.type == EnumTypeOG.music_album and open_graph.music_album:
            open_graph.music_album[-1].song_disc = int(tag.content)
            return True
        if open_graph.type == EnumTypeOG.music_playlist and open_graph.music_play_list:
            open_graph.music_play_list[-1].song_disc = int(tag.content)
            return True
    return False


def music_song_track(tag: TagOR, open_graph: OpenGraph) -> bool:
    if tag.content.isdigit() and 1 <= int(tag.content) <= INT_MAX:
        if open_graph.type == EnumTypeOG.music_album and open_graph.music_album:
            open_graph.music_album[-1].song_track = int(tag.content)
            return True
        if open_graph.type == EnumTypeOG.music_playlist and open_graph.music_play_list:
            open_graph.music_play_list[-1].song_track = int(tag.content)
            return True
    return False


def music_release_date(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        if open_graph.music_album:
            open_graph.music_album[-1].release_date = parse_date(tag.content)
            return True
    except ParseError:
        return False
    return False


def music_creator(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.type == EnumTypeOG.music_playlist and open_graph.music_play_list:
        open_graph.music_play_list[-1].creator = get_profile(content=tag.content)
        return True
    if open_graph.type == EnumTypeOG.music_radio_station and open_graph.music_radio_station:
        open_graph.music_radio_station[-1].creator = get_profile(content=tag.content)
        return True
    return False


def video_actor(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    video.type = get_profile(content=tag.content)
    return True


def video_actor_role(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    video.actor_role = tag.content
    return True


def video_director(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    video.director = get_profile(content=tag.content)
    return True


def video_writer(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    video.writer = get_profile(content=tag.content)
    return True


def video_duration(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    if tag.content.isdigit() and 1 <= int(tag.content) <= INT_MAX:
        video.duration = int(tag.content)
        return True
    return False


def video_release_date(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    try:
        video.release_date = parse_date(tag.content)
        return True
    except ParseError:
        return False


def video_tag(tag: TagOR, open_graph: OpenGraph) -> bool:
    video: Optional[Union[VideoMovie, VideoTvShow, VideoEpisode, VideoOther]] = get_video_is_type(open_graph=open_graph)
    if video is None:
        return False
    video.tag.append(tag.content)
    return True


def video_series(tag: TagOR, open_graph: OpenGraph) -> bool:
    if open_graph.video_episode and validate_url(tag.content):
        open_graph.video_episode[-1].series = VideoTvShow(url=tag.content)
        return True
    return False


def article_published_time(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.article.published_time = parse_date(tag.content)
        return True
    except ParseError:
        return False


def article_modified_time(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.article.modified_time = parse_date(tag.content)
        return True
    except ParseError:
        return False


def article_expiration_time(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.article.expiration_time = parse_date(tag.content)
        return True
    except ParseError:
        return False


def article_author(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.article.author.append(Profile(first_name=tag.content))
    return True


def article_section(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.article.section = tag.content
    return True


def article_tag(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.article.tag.append(tag.content)
    return True


def book_author(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.book.author.append(get_profile(content=tag.content))
    return True


def book_isbn(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.book.isbn = tag.content
    return True


def book_release_date(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.book.release_date = parse_date(tag.content)
        return True
    except ParseError:
        return False


def book_tag(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.book.tag.append(tag.content)
    return True


def profile_first_name(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.profile.first_name = tag.content
    return True


def profile_last_name(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.profile.last_name = tag.content
    return True


def profile_username(tag: TagOR, open_graph: OpenGraph) -> bool:
    open_graph.profile.username = tag.content
    return True


def profile_gender(tag: TagOR, open_graph: OpenGraph) -> bool:
    try:
        open_graph.profile.gender = EnumGender(tag.content)
        return True
    except ValueError:
        return False
