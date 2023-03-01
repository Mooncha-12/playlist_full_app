from typing import List, Optional

from pydantic import BaseModel


class SongBase(BaseModel):
    name: str
    duration: int


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: int
    playlist_id: int

    class Config:
        orm_mode = True


class PlaylistBase(BaseModel):
    name: str


class PlaylistCreate(PlaylistBase):
    name: str


class Playlist(PlaylistBase):
    id: int
    songs: List[Song] = []

    class Config:
        orm_mode = True

class SongUpdate(BaseModel):
    name: str
    duration: int

class SongRequest(BaseModel):
    name: str
    duration: int