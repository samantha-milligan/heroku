import json
import requests


class Playlist:

	def __init__(self, name):
		# will need to add settings_flags as a class variable later

		self.id = None
		self.name = name
		self.description = None
		self.public_flag = False

	def get_id(self):
		return self.id

	def get_settings(self):
		return self.settings_flags

	def create_playlist(self, user_id, spotify_token):
	    # creates empty playlist

	    # call to Spotify API using user account id 
	    query = 'https://api.spotify.com/v1/users/{}/playlists'.format(user_id)

	    # collects all playlist info to pass into request
	    data = json.dumps({
	        'name': self.name,
	        'description': self.description,
	        'public': self.public_flag
	    })

	    # uses token to verify authorization
	    headers = {
	        'Content-Type': 'application/json',
	        'Authorization': 'Bearer {}'.format(spotify_token)
	    }

	    # completes request to Spotify API
	    response = requests.post(
	        query,
	        data=data,
	        headers=headers
	    )

	    # correctly format response
	    response = response.json()

	    # get playlist id from Spotify API call
	    self.id = response['id']
