from django.core.validators import RegexValidator
from core.models import PaymentMethod
from django.forms import ModelForm, widgets
from django.core.validators import MinLengthValidator, MaxLengthValidator

class PaymentForm(ModelForm):

    class Meta:
        #cvc_validator = RegexValidator(
       #     regex=r'^\d{3}$',
       #     message="CVC must be a 3-digit number."
       # )
       # card_number_validator = MinLengthValidator(16, message="Card number must be at least 16 digits.")
       # card_number_validator = MaxLengthValidator(19, message="Card number must be at most 19 digits.")

        model = PaymentMethod
        exclude = ['id']
        widgets = {
            'User': widgets.NumberInput(attrs={'class': 'user_id'}),
            'Card_Number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Exp_Month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Exp_Year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }
        #validators = {
        #    'Card_Number': [card_number_validator],
        #    'Cvc': [cvc_validator]
        #}

    def set_user(self, user_id):
        self.initial['User'] = user_id

    def user(self):
        return self['User']

