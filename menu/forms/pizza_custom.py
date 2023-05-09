from django.forms import ModelForm, widgets
from menu.models import Pizza
class PizzaCreateCustom(ModelForm):
    class Meta:
       model = Pizza
       exclude = ['id']
       widgets = {
           'name' : widgets.TextInput(attrs={'class': 'form-control'}),
       }