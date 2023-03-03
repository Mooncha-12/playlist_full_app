from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models
from sql_app import shemas
from sql_app.database import SessionLocal, engine
from all_about_playlist import Operation, Song, DoublyLinkedList


operation = Operation()

def get_player():
    player = DoublyLinkedList()
    return player

shemas.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Для проверки удаления песни во время проигрывания
check = True


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/playlists/", response_model=models.Playlist)
def create_playlist(playlist: models.PlaylistCreate, db: Session = Depends(get_db)):
    db_playlist = crud.get_playlist_by_name(db, name=playlist.name)
    if db_playlist:
        raise HTTPException(status_code=400, detail="Playlist already there are")
    return crud.create_playlist(db=db, playlist=playlist)


@app.get("/playlists/", response_model=List[models.Playlist])
def read_playlist(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    playlists = crud.get_playlists(db, skip=skip, limit=limit)
    return playlists


@app.get("/playlists/{playlist_id}", response_model=models.Playlist)
def read_playlist_by_id(playlist_id: int, db: Session = Depends(get_db)):
    db_playlist = crud.get_playlist(db, playlist_id=playlist_id)
    if db_playlist is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_playlist


@app.post("/songs/", response_model=models.Song)
def create_song_for_playlist(song: models.SongCreate, db: Session = Depends(get_db)):
    def add_song_for_doublylinkedlist(new_song: models.SongBase):
        s = Song(new_song.name, new_song.duration)
        operation.add_song(s)
        operation.set_current_node(operation.playlist.head)

    new_song = crud.create_playlist_songs(db=db, song=song)
    add_song_for_doublylinkedlist(new_song)
    return new_song



@app.get("/songs/{song_id}", response_model=models.Song)
def read_song_by_id(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.get_song_by_id(db, song_id=song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song


@app.put("/playlists/{song_id}", response_model=models.Song)
def update_song_in_playlist(song_id: int, song: models.SongUpdate, db: Session = Depends(get_db)):
    db_song = crud.update_song(db, song_id, song)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song


@app.delete("/playlists/{playlist_id}")
def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = crud.get_playlist(db, playlist_id=playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist not found")
    crud.delete_playlist_by_id(db, playlist=playlist)
    return {"message": "Playlist deleted successfully"}


@app.delete("/songs/{song_name}")
def delete_song(name: str, db: Session = Depends(get_db), player: DoublyLinkedList = Depends(get_player)):
    global check
    song = crud.get_song_for_delete(db, name=name)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")

    if not check and operation.current_song.name == name:
        check = True
        raise HTTPException(status_code=400, detail="Cannot delete song while it is being played")

    player.delete_node(song)
    crud.delete_song_by_name(db, song=song)
    return {"message": "Song deleted successfully"}


@app.post("/play")
def play():
    global check
    if operation.playlist.length == 0:
        return {"status": "error", "message": "Playlist is empty."}

    operation.play()
    check = False
    return {"status": "playing"}
@app.post("/pause")
def pause():
    if operation.playlist.length == 0:
        return {"status": "error", "message": "Playlist is empty."}

    operation.pause()
    return {"status": "pause"}

@app.post("/next")
def next_song():
    if operation.current_node is None:
        return {"status": "error", "message": "Pointer to the next element is None"}
    operation.next_song()
    return {"status": "the following song is playing"}

@app.post("/previous")
def previous_song():
    if operation.current_node is None:
        return {"status": "error", "message": "Pointer to the previous element is None"}
    operation.previous_song()
    return {"status": "the previous song is playing"}

