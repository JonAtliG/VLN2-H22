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

    def name(self):
        return self['name']

    def meat(self):
        return [self['Bacon'], self['Chicken'], self['Ham'], self['Pepperoni']]

    def greens(self):
        return [self['Jalapeno'], self['Mushrooms'], self['Onion'], self['Paprika'], self['Pineapple']]

    def cheese(self):
        return [self['Cheese'], self['Mozzarella'], self['Pepper_Cheese'], self['Yellow_Cheese']]

    def sauce(self):
        return [self['Pizza_Sauce'], self['Mozzarella'], self['Pepper_Cheese'], self['Yellow_Cheese']]

