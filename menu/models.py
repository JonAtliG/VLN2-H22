from django.db import models


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models:Charfield(max_length=999, blank=True)
    img = models.CharField(max_length=9999, blank=True)
    price = models.FloatField()



class Topping(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)
>>>>>>> f175445f3af19f9e72c98dc951752492d0cbc292
