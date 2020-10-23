from enum import Enum
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class EnumTypeOG(str, Enum):
    article: str = 'article'
    book: str = 'book'
    profile: str = 'profile'
    website: str = 'website'
    music_song: str = 'music.song'
    music_album: str = 'music.album'
    music_playlist: str = 'music.playlist'
    music_radio_station: str = 'music.radio_station'
    video_movie: str = 'video.movie'
    video_episode: str = 'video.episode'
    video_tv_show: str = 'video.tv_show'
    video_other: str = 'video.other'


class EnumGender(str, Enum):
    male: str = 'male'
    female: str = 'female'


class EnumDeterminer(str, Enum):
    a: str = 'a'
    an: str = 'an'
    auto: str = 'auto'
    default: str = ''


class Profile(BaseModel):
    first_name: Optional[str] = Field(default=None, description='Имя пользователя профайла')
    last_name: Optional[str] = Field(default=None, description='Фамилия пользователя профайла')
    username: Optional[str] = Field(default=None, description='Ник')
    gender: Optional[EnumGender] = Field(default=None, description='Пол (мужской, женский) = male/female')
    url: Optional[str] = Field(default=None, description='Url')


class Article(BaseModel):
    published_time: Optional[datetime] = Field(default=None, description='Когда статья была впервые опубликована')
    modified_time: Optional[datetime] = Field(default=None, description='Когда статья была последний раз изменена')
    expiration_time: Optional[datetime] = Field(default=None, description='Время истечения срока статьи')
    author: List[Profile] = Field(default_factory=list, description='Авторы статьи')
    section: Optional[str] = Field(default=None, description='Название категории')
    tag: List[str] = Field(default_factory=list, description='Теги, связанные с этой статьей')
    url: Optional[str] = Field(default=None, description='Url')


class Book(BaseModel):
    author: List[Profile] = Field(default_factory=list, description='Кто написал эту книгу')
    isbn: Optional[str] = Field(default=None, description='Международный стандартный книжный номер ISBN')
    release_date: Optional[datetime] = Field(default=None, description='Дата выпуска книги')
    tag: List[str] = Field(default_factory=list, description='Теги, связанные с этой книгой')
    url: Optional[str] = Field(default=None, description='Url')


class Website(BaseModel):
    pass


# URI: http://ogp.me/ns/music#


class MusicSong(BaseModel):
    duration: Optional[int] = Field(default=None, description='Длина песни в секундах')
    album: List['MusicAlbum'] = Field(default_factory=list, description='Название альбома')
    album_disc: Optional[int] = Field(default=None, description='Номер альбома на диске')
    album_track: Optional[int] = Field(default=None, description='Номер трека в альбоме')
    musician: List[Profile] = Field(default_factory=list, description='Исполнитель песни')
    url: Optional[str] = Field(default=None, description='Url')


class MusicAlbum(BaseModel):
    song: Optional['MusicSong'] = Field(default=None, description='Название песни в альбоме')
    song_disc: Optional[int] = Field(default=None, description='Номер альбома на диске в обратном значении')
    song_track: Optional[int] = Field(default=None, description='Номер трека в альбоме в обратном значении')
    musician: Optional[Profile] = Field(default=None, description='Профайл музыканта, который создал эту песню')
    release_date: Optional[datetime] = Field(default=None, description='Датa выпуска альбома')
    url: Optional[str] = Field(default=None, description='Url')


class MusicPlayList(BaseModel):
    song: Optional['MusicSong'] = Field(default=None, description='Название песни в альбоме')
    song_disc: Optional[int] = Field(default=None, description='Номер альбома на диске в обратном значении')
    song_track: Optional[int] = Field(default=None, description='Номер трека в альбоме в обратном значении')
    creator: Optional[Profile] = Field(default=None, description='Создатель плейлиста')
    url: Optional[str] = Field(default=None, description='Url')


class MusicRadioStation(BaseModel):
    creator: Optional[Profile] = Field(default=None, description='')
    url: Optional[str] = Field(default=None, description='Url')


# URI: https://ogp.me/ns/video#

class VideoMovie(BaseModel):
    actor: List[Profile] = Field(default_factory=list, description='Актеры в этом фильме')
    actor_role: Optional[str] = Field(default=None, description='Роли актеров')
    director: List[Profile] = Field(default_factory=list, description='Режиссеры фильма')
    writer: List[Profile] = Field(default_factory=list, description='Авторы фильма')
    duration: Optional[int] = Field(default=None, description='Длина фильма в секундах')
    release_date: Optional[datetime] = Field(default=None, description='Дата выхода фильма в прокат')
    tag: List[str] = Field(default_factory=list, description='Теги, связанные с этим фильмом')
    url: Optional[str] = Field(default=None, description='Url')


class VideoTvShow(VideoMovie):
    pass


class VideoEpisode(VideoMovie):
    series: Optional[VideoTvShow] = Field(default=None, description='К какой серии этот эпизод принадлежит')


class VideoOther(VideoMovie):
    pass


class OpenGraphImage(BaseModel):
    url: Optional[str] = Field(default=None, description='Идентичный og:image')
    secure_url: Optional[str] = Field(default=None, description='Альтернативный url-адрес')
    type: Optional[str] = Field(default=None, description='Типы MIME для изображения')
    width: Optional[int] = Field(default=None, description='Число пикселей в ширину')
    height: Optional[int] = Field(default=None, description='Число пикселей в высоту')
    alt: Optional[str] = Field(default=None, description='')


class OpenGraphVideo(BaseModel):
    url: Optional[str] = Field(default=None, description='Идентичный og:image')
    secure_url: Optional[str] = Field(default=None, description='Альтернативный url-адрес')
    type: Optional[str] = Field(default=None, description='Типы MIME для изображения')
    width: Optional[int] = Field(default=None, description='Число пикселей в ширину')
    height: Optional[int] = Field(default=None, description='Число пикселей в высоту')


class OpenGraphAudio(BaseModel):
    url: Optional[str] = Field(default=None, description='Идентичный og:image')
    secure_url: Optional[str] = Field(default=None, description='Альтернативный url-адрес')
    type: Optional[str] = Field(default=None, description='Типы MIME для изображения')
    alt: Optional[str] = Field(default=None, description='')


class OpenGraph(BaseModel):
    title: Optional[str] = Field(default=None, description='Название объекта')
    type: EnumTypeOG = Field(default=EnumTypeOG.website, description='Тип объекта')
    url: Optional[str] = Field(default=None, description='Канонический URL-адрес объекта')

    images: List[OpenGraphImage] = Field(default_factory=list, description='')
    videos: List[OpenGraphVideo] = Field(default_factory=list, description='')
    audios: List[OpenGraphAudio] = Field(default_factory=list, description='')

    description: Optional[str] = Field(default=None, description='')
    determiner: Optional[EnumDeterminer] = Field(default=None, description='')
    locale: str = Field(default='en_US', description='Тег локации. Формат language_TERRITORY')
    locale_alternate: List[str] = Field(default_factory=list, description='')
    site_name: Optional[str] = Field(default=None, description='')

    music_song: List[MusicSong] = Field(default_factory=list, description='')
    music_album: List[MusicAlbum] = Field(default_factory=list, description='')
    music_play_list: List[MusicPlayList] = Field(default_factory=list, description='')
    music_radio_station: List[MusicRadioStation] = Field(default_factory=list, description='')

    video_movie: List[VideoMovie] = Field(default_factory=list, description='')
    video_tv_show: List[VideoTvShow] = Field(default_factory=list, description='')
    video_episode: List[VideoEpisode] = Field(default_factory=list, description='')
    video_other: List[VideoOther] = Field(default_factory=list, description='')

    profile: Profile = Field(default_factory=Profile, description='')
    article: Article = Field(default_factory=Article, description='')
    book: Book = Field(default_factory=Book, description='')
    website: Website = Field(default_factory=Website, description='')


MusicSong.update_forward_refs()

if __name__ == '__main__':
    pass
