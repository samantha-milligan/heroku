import json
import requests


class Song:

    def __init__(self, playlist):
        self.playlist_id = playlist.id


    def find_songs(self):
        # uses location and settings_flags to find songs
        # may need to add location and settings_flags as class variables
        # uses Shazam API

        # currently hardcoded values
        # song_list must be in format [(song, artist)]
        # can add name and artist as class variables
        song_list = [('Crew', 'Brent Faiyaz'), ('Si Una Vez', 'Selena')]

        return song_list

    def get_song_uris(self, song_list, spotify_token):
        # collects all uris using song info and returns list

        # create list to add all uris
        song_uris_list = []

        # loop over all songs in song list
        for song in song_list:
            # call to Spotify API using song name and artist
            name = song[0]
            artist = song[1]
            query = 'https://api.spotify.com/v1/search?q={},{}&type=track%2Cartist&limit=1'.format(name, artist)

            # uses token to verify authorization
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(spotify_token)
            }

            # completes request to Spotify API
            response = requests.get(
                query,
                headers=headers
            )

            response = response.json()

            # collect song uri
            song_uri = response['tracks']['items'][0]['uri']

            # append to song list
            song_uris_list.append(song_uri)

        return song_uris_list


    def add_songs(self, song_uris_list, spotify_token):
        # add songs to any playlist using playlist id

        # call to Spotify API
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(self.playlist_id)

        # collects all song uris to pass into request
        data = json.dumps(song_uris_list)

        # uses token to verify authorization
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(spotify_token)
        }

        # completes request to Spotify API, songs are now added to playlist
        response = requests.post(
            query,
            data=data,
            headers=headers
        )
