class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        
class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
        print("Title", song.title)

class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        print("Play Musik")
        
        
song1 = Song("Let Her Go", "Eminem")
song2 = Song("Angel Baby", "Adele")
playlist = Playlist()
playlist.add_song(song1)
playlist.add_song(song2)
media_player = MediaPlayer(playlist)
media_player.playlist.songs
