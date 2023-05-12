from core.models import PaymentMethod
from django.forms import ModelForm, widgets
from django import forms


class PaymentForm(ModelForm):
    Card_Number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PaymentMethod
        exclude = ['id']
        widgets = {
            'User': widgets.NumberInput(attrs={'class': 'user_id'}),
            #'Card_Number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Exp_Month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Exp_Year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        exp_month = cleaned_data.get('Exp_Month')
        exp_year = cleaned_data.get('Exp_Year')
        card_number = cleaned_data.get('Card_Number')
        cvc = cleaned_data.get('Cvc')

        if exp_month is not None and (exp_month < 1 or exp_month > 12):
            self.add_error('Exp_Month', 'Invalid month, has to be between 01 and 12.')
        if exp_year is not None and (exp_year < 23 or exp_year > 99):
            self.add_error('Exp_Year', 'Invalid year. Input as two digits and not before year 23')
        if card_number is not None and (len(str(card_number)) < 13 or len(str(card_number)) > 16):
            self.add_error('Card_Number', 'Invalid card number, has to be between 13-16 digits.')
        if cvc is not None and len(str(cvc)) != 3:
            self.add_error('Cvc', 'Invalid CVC, has must be a 3 digits long.')
        return cleaned_data

    def set_user(self, user_id):
        self.initial['User'] = user_id

    def user(self):
        return self['User']

