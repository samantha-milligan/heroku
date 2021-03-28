

class Account:

	def __init__(self, user_id, spotify_token):
		self.user_id = user_id
		self.spotify_token = spotify_token
		self.user_type = None
		self.location = None

	def get_user_id(self):
		return self.user_id

	def get_spotify_token(self):
		return self.spotify_token

	def get_user_type(self):
		return self.user_type

	def get_location(self):
		return self.location

	def validate_user(self):
		# TODO
		pass

	def validate_spotify_info(self):
		# TODO
		pass
