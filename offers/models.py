from django.db import models


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)

class OnPizza(models.Model):


class Topping(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)



class Drinks(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)


class Sides(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    img = models.CharField(max_length=9999, blank=True)


class Address(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.IntegerField()
    country = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=255)


class CardInfo(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.IntegerField()
    exp_date = models.DateField()
    cvc = models.IntegerField()
