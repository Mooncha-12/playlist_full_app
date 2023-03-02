from fastapi.testclient import TestClient
from app.main import app
import httpx

client = TestClient(app)


def test_create_playlist():
    data = {"name": "Test Playlist"}
    response = client.post("/playlists", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "Test Playlist", "id": 1}


def test_read_playlist():
    response = client.get("/playlists")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Playlist", "id": 1}


def test_read_playlist_by_id():
    response = client.get("/playlists/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Playlist", "id": 1}

def test_create_song_for_playlist():
    data = {"name": "Test Song", "duration": 20}
    response = client.post("/songs/", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "Test Song", "id": 1}


