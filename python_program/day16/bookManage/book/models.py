from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    author = models.CharField(max_length=32)
    publiosh = models.CharField(max_length=32)
    info = models.CharField(max_length=1024)
