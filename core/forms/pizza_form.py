from django.forms import ModelForm, widgets
from core.models import Pizza


class PizzaCreateForm(ModelForm):
    class Meta:
        model = Pizza
        exclude = ['id', 'img']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Custom pizza'}),
            'Bacon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Chicken': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Ham': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Pepperoni': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Jalapeno': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Mushrooms': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Onion': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Paprika': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Pineapple': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Cheese': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Mozzarella': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Pepper_Cheese': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Yellow_Cheese': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'Pizza_Sauce': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
        }
