from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils.account import Account
from .utils.playlist import Playlist
from .utils.song import Song


class PlaylistView(APIView):

    def get(self, request):
        # Creates playlist and adds songs using user and playlist info

        # get user id and spotify token from request
        user_id = request.query_params.get('user_id')
        spotify_token = request.query_params.get('auth_token')
        account = Account(user_id, spotify_token)

        # get playlist name from request
        playlist_name = request.query_params.get('playlist_name')
        playlist = Playlist(playlist_name)

        # create empty playlist
        playlist.create_playlist(user_id, spotify_token)

        song = Song(playlist)
        song_list = song.find_songs()
        song_uris_list = song.get_song_uris(song_list, spotify_token)
        # add songs to playlist
        song.add_songs(song_uris_list, spotify_token)

        # return playlist id to embed into website
        response = Response(playlist.get_id())
        response['Access-Control-Allow-Origin'] = '*'

        return response
