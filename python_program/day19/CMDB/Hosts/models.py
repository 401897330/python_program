from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Hosts(models.Model):
    ip = models.CharField(max_length=32)
    port = models.IntegerField()
    doman = models.CharField(max_length=32)
    service_line = models.ForeignKey("Service")

class User(models.Model):
    name = models.CharField(max_length=18)
    password = models.CharField(max_length=64)
    e_mail = models.EmailField()
    service = models.ManyToManyField("Service")