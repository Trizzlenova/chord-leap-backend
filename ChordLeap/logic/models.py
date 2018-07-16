from django.db import models
from logic.auth import *

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    full_name = models.CharField(max_length=40, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username


class Chord(models.Model):
    name = models.CharField(max_length=10)
    related_chords = models.CharField(max_length=120)


    def __str__(self):
        return self.name


class Progression(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    # Change to chord model object
    chords = models.ManyToManyField(Chord, related_name='chords')
    array_of_chords = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.user




# Progression.objects.create(user: id, chords: array of strings)
