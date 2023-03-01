from fastapi import HTTPException

from sqlalchemy.orm import Session

from app import models
from sql_app import shemas

def get_playlist(db: Session, playlist_id: int):
    return db.query(shemas.Playlist).filter(shemas.Playlist.id == playlist_id).first()


def get_playlist_by_name(db: Session, name: str):
    return db.query(shemas.Playlist).filter(shemas.Playlist.name == name).first()


def get_playlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(shemas.Playlist).offset(skip).limit(limit).all()


def create_playlist(db: Session, playlist: models.PlaylistCreate):
    existing_playlist = db.query(shemas.Playlist).all()
    if existing_playlist:
        raise HTTPException(status_code=400, detail="Cannot create new playlists")
    db_playlist = shemas.Playlist(name=playlist.name)
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist


def get_song(db: Session, song_id: int):
    return db.query(shemas.Song).filter(shemas.Song.id == song_id).first()


def create_playlist_songs(db: Session, song: models.SongCreate):
    playlist = db.query(shemas.Playlist).first()
    db_song = shemas.Song(**song.dict(), playlist_id=playlist.id)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

def delete_playlist_by_id(db: Session, playlist: models.Playlist):
    db.delete(playlist)
    db.commit()


def delete_song_by_id(db: Session, song: models.Song):
    db.delete(song)
    db.commit()

def update_song(db: Session, song_id: int, song: models.SongUpdate):
    db_song = db.query(shemas.Song).filter(shemas.Song.id == song_id).first()
    if not db_song:
        return None
    update_data = song.dict(exclude_unset=True)
    for attr, value in update_data.items():
        if value is not None:
            setattr(db_song, attr, value)
    db.commit()
    db.refresh(db_song)
    return db_song