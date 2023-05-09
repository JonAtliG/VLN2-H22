from django.db import models


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)
