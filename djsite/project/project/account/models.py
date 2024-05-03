from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class ShopUser(AbstractBaseUser):
    username = models.CharField(max_length=6, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"Client numer: {self.username} Email: {self.email}"
