from iso8601 import parse_date, ParseError

from src.apps.models.parsers.tags import TagOR
from src.apps.models.open_graph import OpenGraph, EnumTypeOG, EnumDeterminer, EnumGender, OpenGraphImage, \
    OpenGraphAudio, OpenGraphVideo, Profile


def og_title(tag: TagOR, og: OpenGraph) -> bool:
    og.title = tag.content
    return True


def og_determiner(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.description = EnumDeterminer(tag.content)
        return True
    except ValueError as e:
        return False


def og_description(tag: TagOR, og: OpenGraph) -> bool:
    og.description = tag.content
    return True


def og_site_name(tag: TagOR, og: OpenGraph) -> bool:
    og.site_name = tag.content
    return True


def og_url(tag: TagOR, og: OpenGraph) -> bool:
    og.url = tag.content
    return True


def og_locale(tag: TagOR, og: OpenGraph) -> bool:
    og.locale = tag.content
    return True


def og_locale_alternate(tag: TagOR, og: OpenGraph) -> bool:
    og.locale_alternate.append(tag.content)
    return True


def og_type(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.type = EnumTypeOG(tag.content)
        return True
    except ValueError as e:
        return False


def og_image(tag: TagOR, og: OpenGraph) -> bool:
    og.images.append(OpenGraphImage(url=tag.content))
    return True


def og_image_secure_url(tag: TagOR, og: OpenGraph) -> bool:
    if og.images:
        og.images[-1].secure_url = tag.content
        return True
    else:
        return False


def og_image_type(tag: TagOR, og: OpenGraph) -> bool:
    if og.images:
        og.images[-1].type = tag.content
        return True
    else:
        return False


def og_image_width(tag: TagOR, og: OpenGraph) -> bool:
    if og.images and tag.content.isdecimal():
        og.images[-1].width = int(tag.content)
        return True
    else:
        return False


def og_image_height(tag: TagOR, og: OpenGraph) -> bool:
    if og.images and tag.content.isdecimal():
        og.images[-1].height = int(tag.content)
        return True
    else:
        return False


def og_image_alt(tag: TagOR, og: OpenGraph) -> bool:
    if og.images:
        og.images[-1].alt = tag.content
        return True
    else:
        return False


def og_audio(tag: TagOR, og: OpenGraph) -> bool:
    og.audios.append(OpenGraphAudio(url=tag.content))
    return True


def og_audio_secure_url(tag: TagOR, og: OpenGraph) -> bool:
    if og.audios:
        og.audios[-1].secure_url = tag.content
        return True
    else:
        return False


def og_audio_type(tag: TagOR, og: OpenGraph) -> bool:
    if og.audios:
        og.audios[-1].type = tag.content
        return True
    else:
        return False


def og_audio_alt(tag: TagOR, og: OpenGraph) -> bool:
    if og.audios:
        og.audios[-1].alt = tag.content
        return True
    else:
        return False


def og_video(tag: TagOR, og: OpenGraph) -> bool:
    og.videos.append(OpenGraphVideo(url=tag.content))
    return True


def og_video_secure_url(tag: TagOR, og: OpenGraph) -> bool:
    if og.videos:
        og.videos[-1].secure_url = tag.content
        return True
    else:
        return False


def og_video_type(tag: TagOR, og: OpenGraph) -> bool:
    if og.videos:
        og.videos[-1].type = tag.content
        return True
    else:
        return False


def og_video_width(tag: TagOR, og: OpenGraph) -> bool:
    if og.videos and tag.content.isdigit():
        og.videos[-1].width = tag.content
        return True
    else:
        return False


def og_video_height(tag: TagOR, og: OpenGraph) -> bool:
    if og.videos and tag.content.isdigit():
        og.videos[-1].height = tag.content
        return True
    else:
        return False


def music_duration(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_album(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_album_disc(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_album_track(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_musician(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_song(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_song_disc(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_song_track(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_release_date(tag: TagOR, og: OpenGraph) -> bool:
    return False


def music_creator(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_actor(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_actor_role(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_director(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_writer(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_duration(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_release_date(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_tag(tag: TagOR, og: OpenGraph) -> bool:
    return False


def video_series(tag: TagOR, og: OpenGraph) -> bool:
    return False


def article_published_time(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.article.published_time = parse_date(tag.content)
        return True
    except ParseError as e:
        return False


def article_modified_time(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.article.modified_time = parse_date(tag.content)
        return True
    except ParseError as e:
        return False


def article_expiration_time(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.article.expiration_time = parse_date(tag.content)
        return True
    except ParseError as e:
        return False


def article_author(tag: TagOR, og: OpenGraph) -> bool:
    og.article.author.append(Profile(first_name=tag.content))
    return True


def article_section(tag: TagOR, og: OpenGraph) -> bool:
    og.article.section = tag.content
    return True


def article_tag(tag: TagOR, og: OpenGraph) -> bool:
    og.article.tag.append(tag.content)
    return True


def book_author(tag: TagOR, og: OpenGraph) -> bool:
    og.book.author.append(Profile(first_name=tag.content))
    return True


def book_isbn(tag: TagOR, og: OpenGraph) -> bool:
    og.book.isbn = tag.content
    return True


def book_release_date(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.book.release_date = parse_date(tag.content)
        return True
    except ParseError as e:
        return False


def book_tag(tag: TagOR, og: OpenGraph) -> bool:
    og.book.tag.append(tag.content)
    return True


def profile_first_name(tag: TagOR, og: OpenGraph) -> bool:
    og.profile.first_name = tag.content
    return True


def profile_last_name(tag: TagOR, og: OpenGraph) -> bool:
    og.profile.last_name = tag.content
    return True


def profile_username(tag: TagOR, og: OpenGraph) -> bool:
    og.profile.username = tag.content
    return True


def profile_gender(tag: TagOR, og: OpenGraph) -> bool:
    try:
        og.profile.gender = EnumGender(tag.content)
        return True
    except ValueError as e:
        return False

