from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
