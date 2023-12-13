from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	phone = models.CharField(max_length=20)
	photo = models.ImageField(upload_to = 'user_photo')

	STATUS = (
		('admin', 'ADMIN'),
		('manager', 'MANAGER'),
		('user', 'USER'),
		)


	address = models.CharField(max_length = 30, null = True)
	phone = models.CharField(max_length = 13)
	image = models.ImageField(upload_to = 'user_photos/', null = True, blank = True)
	status = models.CharField(max_length = 10, choices = STATUS, default = 'user')

	def __str__(self):
		return self.username
