import requests

class libraryClient():
    def __init__(self, base_url):
        self.base_url = base_url

    def create_playlist(self, name):
        url = f"{self.base_url}/playlists"
        data = {"name": name}
        responce = requests.post(url, json=data)

        return responce

    def get_playlist(self, playlist_id):
        url = f"{self.base_url}/playlists/{playlist_id}"
        responce = requests.get(url)
        responce.raise_for_status()
        return responce.json()

    def get_playlist_by_id(self, playlist_id):
        url = f"{self.base_url}/playlists/{playlist_id}"
        responce = requests.get(url)

        return responce.status_code

    def create_song_for_playlist(self, name, duration):
        url = f"{self.base_url}/songs"
        data = {"name": name, "duration": duration}
        responce = requests.post(url, json=data)

        return responce.status_code

    def get_song(self, song_id):
        url = f"{self.base_url}/songs/{song_id}"
        responce = requests.get(url)
        return responce.status_code

    def update_song(self, song_id, name, duration):
        data = {"name": name, "duration": duration}
        url = f"{self.base_url}/playlists/{song_id}"
        responce = requests.put(url, data)
        responce.raise_for_status()
        return responce.status_code

client = libraryClient("http://localhost:8000")
playlist = client.create_playlist("playlist")
p = playlist.json()
if playlist.status_code == 200:
    print("ok")


playlist_id = p["id"]
p = client.get_playlist(playlist_id)
if playlist.status_code == 200:
    print(playlist.json())

