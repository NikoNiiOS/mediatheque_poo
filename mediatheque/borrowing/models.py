from django.db import models
from media.models import Media
from users.models import User

class Borrowing(models.Model):
    media = models.ForeignKey(Media, null=True, on_delete=models.SET_NULL)
    emprunteur = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True)