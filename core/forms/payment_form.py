from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import PaymentMethod
from django.forms import ModelForm, widgets

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentMethod
        exclude = ['user']
        widgets = {
            'Card_Number': widgets.TextInput(attrs={'class': 'form-control'}),
            'Exp_Date': widgets.TextInput(attrs={'class': 'form-control'}),
            'Cvc': widgets.TextInput(attrs={'class': 'form-control'})
        }

    def set_user(self, user_id):
        self.initial['User'] = user_id