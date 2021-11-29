from django.db import models
from accounts.models import User


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField('Title', max_length=50)
	content = models.TextField()
	slug = models.SlugField()
	img = models.ImageField(upload_to="post", null=True)
	created = models.DateTimeField(auto_now=True)
	update = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
