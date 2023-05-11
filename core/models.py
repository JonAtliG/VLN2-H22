from django.db import models
from dbview.models import DbView
from django.contrib.auth.models import User as BaseUserClass
from django.contrib.contenttypes import fields
from django_countries.fields import CountryField


class User(BaseUserClass):
    Phone_Number = models.IntegerField(blank=False)
    Profile_picture = models.CharField(max_length=9999)
    Street_Name = models.CharField(max_length=255)
    House_Number = models.IntegerField(max_length=5)
    Country = CountryField()
    Postal_Code = models.IntegerField(max_length=5)
    City = models.CharField(max_length=255)

class Pizza(models.Model):
    User = models.ForeignKey(BaseUserClass, blank=True, null=True, on_delete=models.CASCADE)
    img = models.CharField(max_length=999, blank=True)
    name = models.CharField(max_length=255)
    Bacon = models.BooleanField(default=False)
    Chicken = models.BooleanField(default=False)
    Ham = models.BooleanField(default=False)
    Pepperoni = models.BooleanField(default=False)
    Jalapeno = models.BooleanField(default=False)
    Mushrooms = models.BooleanField(default=False)
    Onion = models.BooleanField(default=False)
    Paprika = models.BooleanField(default=False)
    Pineapple = models.BooleanField(default=False)
    Cheese = models.BooleanField(default=False)
    Mozzarella = models.BooleanField(default=False)
    Pepper_Cheese = models.BooleanField(default=False)
    Yellow_Cheese = models.BooleanField(default=False)
    Pizza_Sauce = models.BooleanField(default=False)


class Side(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=999, blank=True)
    desc = models.CharField(max_length=999, blank=True)
    price = models.FloatField()


class Drink(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=999, blank=True)
    desc = models.CharField(max_length=999, blank=True)
    price = models.FloatField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = fields.GenericForeignKey('content_type', 'object_id')

#
#class User(models.Model):
#    name = models.CharField(max_length=255)
#    email = models.CharField(max_length=255)
#    password = models.CharField(max_length=255)
#    phone_number = models.IntegerField()
#    img = models.CharField(max_length=9999, blank=True)
#
#
#class Address(models.Model):
#    name = models.CharField(max_length=255)
#    street = models.CharField(max_length=255)
#    house_number = models.IntegerField()
#    country = models.CharField(max_length=255)
#    postal_code = models.IntegerField()
#    city = models.CharField(max_length=255)
#
#
#class UserAddress(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE())
#    address = models.ForeignKey(Address, on_delete=models.CASCADE())
#
#
#class CardInfo(models.Model):
#    name = models.CharField(max_length=255)
#    card_number = models.IntegerField()
#    exp_date = models.DateField()
#    cvc = models.IntegerField()
#