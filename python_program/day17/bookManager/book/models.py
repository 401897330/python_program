from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=32)


class Publish(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    info = models.CharField(max_length=1024)
    author = models.ForeignKey(Author)
    publish = models.ForeignKey(Publish)


