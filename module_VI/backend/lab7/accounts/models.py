from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	# Extendiendo el modelo "User" que viene por defecto en django

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to="images", blank=True)

	def __unicode__(self):
		return self.user.username