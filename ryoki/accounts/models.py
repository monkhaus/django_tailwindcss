from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class User(AbstractUser):
	user_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)
	username = models.CharField(max_length=32, unique=True)
	email = models.EmailField(unique=True)




