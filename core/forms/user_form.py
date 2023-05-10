from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from core.models import User


class Create_Account_Form(UserCreationForm):
    email = forms.EmailField
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,8}$', message='Phone number')
    Phone_Number = forms.CharField(validators=[phone_regex], max_length=8)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'Phone_Number', 'password1', 'password2']
        help_texts = {
            'password2': None,
            'username': None,
        }
