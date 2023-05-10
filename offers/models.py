from django.db import models
from dbview.models import DbView


# Create your models here.

class topping_type(models.Model):
    name = models.CharField(max_length=255)


class topping(models.Model):
    name = models.CharField(max_length=255)
    #img = models.CharField(max_length=9999, blank=True)
    type = models.ForeignKey(topping_type, on_delete=models.CASCADE)


class pizza(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=9999, blank=True)
    toppings = models.ManyToManyField(topping)




#class pizza_view(DbView):
#    @classmethod
#    def get_view_str(cls):
#        return """
#        create view pizza_view as (
#        select * from offers_pizza p
#        join offers_on_pizza o on o.pizza_id = p.id
#        join offers_topping t on o.topping_id = t.id
#        )"""

#class Drinks(models.Model):
#    name = models.CharField(max_length=255)
#    img = models.CharField(max_length=9999, blank=True)
#
#
#class Sides(models.Model):
#    name = models.CharField(max_length=255)
#    img = models.CharField(max_length=9999, blank=True)
#
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