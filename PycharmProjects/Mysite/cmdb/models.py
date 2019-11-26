from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)