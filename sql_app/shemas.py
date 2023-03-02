from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_app.database import Base


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)

    songs = relationship("Song", back_populates="playlist")




class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    duration = Column(Integer, index=True)

    playlist_id = Column(Integer, ForeignKey("playlists.id"))

    playlist = relationship("Playlist", back_populates="songs")