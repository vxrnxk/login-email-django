from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name
