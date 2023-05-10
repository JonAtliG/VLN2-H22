from django.db import models
from dbview.models import DbView


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)


class Topping(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)


class OnPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

class PizzaView(DbView):
    @classmethod
    def get_view_str(cls):
        return """
        create view PizzaView as (
        select * from Pizza p
        join OnPizza o on o.pizza = p.id
        join Topping t on o.topping = t.id
        )"""

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


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    address = models.ForeignKey(Address, on_delete=models.CASCADE())


class CardInfo(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.IntegerField()
    exp_date = models.DateField()
    cvc = models.IntegerField()
