from django.db import models
from django.utils.timezone import timezone

class Login(models.Model):
	Serial_No = models.IntegerField(max_length=100, primary_key=True)
	Family_No = models.IntegerField(max_length=100)
	Email_id = models.EmailField(max_length=100)
	Password = models.CharField(max_length=100)
