from django.db import models
from accounts.models import User

from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=55)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField(max_length=550)

	def __str__(self):
		return self.title



class Idea(models.Model):
	idea_text = models.CharField(max_length=100)
	def __str__(self):
		return self.idea_text

