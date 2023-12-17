from django.db import models

# Create your models here.


class Films(models.Model):
    name = models.CharField(max_length = 255)
    year = models.IntegerField()
    genre = models.ManyToManyField('Genre')

class Genre(models.Model):
    name = models.CharField(max_length = 255)

class Description(models.Model):
    text = models.TextField()
    film = models.OneToOneField(Films,on_delete=models.CASCADE)
    