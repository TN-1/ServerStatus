from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MCServer(models.Model):
    name = models.CharField(max_length=100)
    IPaddress = models.CharField(max_length=15, blank=True)
    domain = models.CharField(max_length=100, blank=True)
    port = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)