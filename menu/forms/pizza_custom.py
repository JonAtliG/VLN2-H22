from django.forms import ModelForm, widgets
from django import forms
from menu.models import Pizza
class PizzaCreateCustom(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    class Meta:
       model = Pizza
       exclude = ['id']
       widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.ChekboxInput(attrs={'class': 'checkbox'})
       }