from django.db import models

class Media(models.Model):
    name = models.fields.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Book(Media):
    auteur = models.fields.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.auteur}"


class Dvd(Media):
    realisateur = models.fields.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.realisateur}"


class Cd(Media):
    artiste = models.fields.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.artiste}"


class JeuDePlateau(models.Model):
    name = models.fields.CharField(max_length=100)
    createur = models.fields.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}, {self.createur}"