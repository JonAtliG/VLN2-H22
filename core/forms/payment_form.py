from django.core.validators import RegexValidator
from core.models import PaymentMethod
from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

class PaymentForm(ModelForm):

    class Meta:
        model = PaymentMethod
        exclude = ['id']
        widgets = {
            'User': widgets.NumberInput(attrs={'class': 'user_id'}),
            'Card_Number': widgets.NumberInput(attrs={'class': 'form-control'}),
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

        # Check exp_month and exp_year are both 2 digits
        if exp_month is not None and (exp_month < 1 or exp_month > 12):
            self.add_error('Exp_Month', 'Invalid month. It must be between 1 and 12.')
        if exp_year is not None and (exp_year < 0 or exp_year > 99):
            self.add_error('Exp_Year', 'Invalid year. It must be a two-digit number.')
        # Check credit card number is between 13-16 digits
        if card_number is not None and (len(str(card_number)) < 13 or len(str(card_number)) > 16):
            self.add_error('Card_Number', 'Invalid card number. It must be between 13 and 16 digits long.')
        # Check cvc is only 3 digits
        if cvc is not None and len(str(cvc)) != 3:
            self.add_error('Cvc', 'Invalid CVC. It must be a 3 digits long.')
        return cleaned_data

    def set_user(self, user_id):
        self.initial['User'] = user_id

    def user(self):
        return self['User']

