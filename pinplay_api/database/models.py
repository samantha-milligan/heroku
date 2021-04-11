from django.db import models


class SpotifySong(models.Model):
	uri = models.CharField(max_length=50)
	location = models.CharField(max_length=20)
	explicit = models.BooleanField()
	genre = models.CharField(max_length=100)

	def __str__(self):
		return self.uri
