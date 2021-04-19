import json
import requests

from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.test import APIClient as Client

from pinplay_api.utils.song import Song


class PinplayTestCase(SimpleTestCase):

    def setUp(self):
        self.client = Client()

        # values must be hardcoded
        self.user_id = 'must be hardcoded'
        self.spotify_token = 'must be hardcoded'
        self.location = 'PHX'
        self.explicit = 'False'
        self.genre = 'pop'

        self.params = {
            'user_id': self.user_id,
            'spotify_token': self.spotify_token,
            'playlist_name': 'Test',
            'location': self.location,
            'explicit': self.explicit,
            'genre': self.genre
        }

        self.response = self.client.get(
            '/pinplay_api/', 
            self.params
        )

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.spotify_token)
        }

    def test_playlist_created(self):
        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)

        request = requests.get(
            query,
            headers=self.headers
        )

        request = request.json()
        playlist_id = request['items'][0]['id']

        self.assertEqual(playlist_id, self.response.data)

    def test_check_tracks(self):
        query = 'https://api.spotify.com/v1/playlists/{}/tracks?market=US'.format(self.response.data)

        request = requests.get(
            query,
            headers=self.headers
        )

        request = request.json()

        track_list = []

        for item in request['items']:
           artist_id = item['track']['artists'][0]['id']
           track_explicit = item['track']['explicit']
           track_list.append((artist_id, track_explicit))

        song = Song(None)
        verified_list = []

        for track in track_list:
            if str(track[1]) == self.explicit:
                track_genre = song.get_genre(track[0], self.spotify_token)
                for item in track_genre:
                    if str(self.genre) in item and track not in verified_list:
                        verified_list.append(track)

        self.assertEqual(len(verified_list), len(track_list))
