from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    info = models.CharField(max_length=1024)
    author = models.ManyToManyField("Author")
    publish = models.ForeignKey("Publish")

class User(models.Model):
    name = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    e_mail = models.EmailField()


