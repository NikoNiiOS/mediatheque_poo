from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    nombreEmprunts = models.IntegerField(default=0)

    def __str__(self):
        """formating string"""
        return f"{self.username}, {self.last_name}, {self.first_name}, {self.is_staff}"