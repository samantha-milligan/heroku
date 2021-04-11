from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pinplay_api.utils.account import Account
from pinplay_api.utils.playlist import Playlist
from pinplay_api.utils.song import Song
from pinplay_api.load_database import add


class PlaylistView(APIView):

    def get(self, request):
        # creates playlist using user info and playlist info

        user_id = request.query_params.get('user_id')
        spotify_token = request.query_params.get('spotify_token')
        account = Account(user_id, spotify_token)

        playlist_name = request.query_params.get('playlist_name')
        playlist = Playlist(playlist_name)

        playlist.create_playlist(user_id, spotify_token)

        song = Song(playlist)
        location = request.query_params.get('location')
        song_list = song.find_songs(location)
        song_info_list = song.get_song_info(song_list, spotify_token)

        explicit = request.query_params.get('explicit')
        genre = request.query_params.get('genre')
        filtered_uris = song.filter_songs(song_info_list, spotify_token, explicit, genre)
        song.add_songs(filtered_uris, spotify_token)

        #add(spotify_token, location)

        response = Response(playlist.get_id())
        response['Access-Control-Allow-Origin'] = '*'

        return response
