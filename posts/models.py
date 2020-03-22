from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

	title=models.CharField(max_length=50)
	link=models.TextField()
	votes=models.IntegerField(default=1)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	pdate=models.DateTimeField()

	def __str__(self):
		return self.title

	def displaydate(self):
		return self.pdate.strftime('%b %d %Y')