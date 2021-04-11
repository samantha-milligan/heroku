from pinplay_api.database.models import SpotifySong
from pinplay_api.utils.song import Song

def add(spotify_token, location):
    song = Song(None)
    song_list = song.find_songs(location)
    song_info_list = song.get_song_info(song_list, spotify_token)

    for item in song_info_list:
        SpotifySong.objects.create(uri=item[0], explicit=item[1], genre=item[2], location=location)
