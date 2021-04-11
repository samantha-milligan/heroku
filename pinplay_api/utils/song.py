import json
import requests

class Song:

    def __init__(self, playlist):
        if playlist == None:
            self.playlist = None
        else:
            self.playlist_id = playlist.id

    def find_songs(self, location):
        song_list = []

        filepath = 'Shazam_' + location +'.csv'
        with open(filepath) as fp:
            for line in fp:
                line = line.strip().split(",")
                song_name = line[2]
                song_artist = line[1]
                song_list.append([song_name, song_artist])

        return song_list

    def get_genre(self, artist_id, spotify_token):
        query = 'https://api.spotify.com/v1/artists/{}'.format(artist_id)

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

        return response['genres']

    def get_song_info(self, song_list, spotify_token):
        # collects all uris using song info and returns list

        # create list to add all uris
        song_info_list = []
        artist_id_list = []

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
            explicit = response['tracks']['items'][0]['explicit']
            artist_id = response['tracks']['items'][0]['artists'][0]['id']

            genre = self.get_genre(artist_id, spotify_token)

            # append to song list
            song_info_list.append([song_uri, explicit, genre])

        return song_info_list

    def filter_songs(self, song_info_list, spotify_token, explicit, genre):
        # need to add genre
        filtered_uris = []

        for song_info in song_info_list:
            for item in song_info[2]:
                if song_info[0] not in filtered_uris and (genre in item or genre == 'none'):
                    if explicit == 'True':
                        filtered_uris.append(song_info[0])
                    else:
                        if song_info[1] == False:
                            filtered_uris.append(song_info[0])

        return filtered_uris

    def add_songs(self, filtered_uris, spotify_token):
        # add songs to any playlist using playlist id

        # call to Spotify API
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(self.playlist_id)

        # collects all song uris to pass into request
        data = json.dumps(filtered_uris)

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
