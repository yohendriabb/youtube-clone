from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
	stripe_id = models.CharField(max_length=50, blank=True, null=True)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField()
	create = models.DateTimeField(auto_now=True)
	profile = models.ImageField(upload_to="userprofile", null=True)
	update = models.DateTimeField(auto_now_add=True)
	followers = models.IntegerField(default=0)
	following = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username
