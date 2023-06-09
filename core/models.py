from django.db import models
from dbview.models import DbView
from django.contrib.auth.models import User as BaseUserClass
from django_countries.fields import CountryField


class User(BaseUserClass):
    Phone_Number = models.IntegerField(blank=False)
    Profile_picture = models.CharField(max_length=9999)
    Street_Name = models.CharField(null=True, blank=True, max_length=255)
    House_Number = models.IntegerField(null=True, blank=True)
    Country = CountryField(null=True, blank=True)
    Postal_Code = models.IntegerField(null=True, blank=True)
    City = models.CharField(null=True, blank=True, max_length=255)


class PaymentMethod(models.Model):
    User = models.ForeignKey(BaseUserClass, on_delete=models.CASCADE)
    Card_Number = models.CharField(max_length=16)
    Exp_Month = models.IntegerField()
    Exp_Year = models.IntegerField()
    Cvc = models.IntegerField()


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

    def toppings(self):
        return {'Bacon': self.Bacon,
                'Chicken': self.Chicken,
                'Ham': self.Ham,
                'Pepperoni': self.Pepperoni,
                'Jalapeno': self.Jalapeno,
                'Mushrooms':self.Mushrooms,
                'Onion': self.Onion,
                'Paprika': self.Paprika,
                'Pineapple': self.Pineapple,
                'Cheese': self.Cheese,
                'Mozzarella': self.Mozzarella,
                'Pepper_Cheese': self.Pepper_Cheese,
                'Yellow_Cheese': self.Yellow_Cheese,
                'Pizza_Sauce': self.Pizza_Sauce}


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


class Offer3For2(models.Model):
    user = models.ForeignKey(BaseUserClass, on_delete=models.CASCADE)
    pizza1 = models.ForeignKey(Pizza, related_name='%(class)s_pizza_1', on_delete=models.CASCADE)
    pizza2 = models.ForeignKey(Pizza, related_name='%(class)s_pizza_2', on_delete=models.CASCADE)
    pizza3 = models.ForeignKey(Pizza, related_name='%(class)s_pizza_3', on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.CASCADE)
    side = models.ForeignKey(Side, null=True, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, null=True, on_delete=models.CASCADE)
    offer_3_for_2 = models.ForeignKey(Offer3For2, null=True, on_delete=models.CASCADE)


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