from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class Create_Account_Form(UserCreationForm):
    email = forms.EmailField
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,8}$', message='Phone number')
    phone_number = forms.CharField(validators=[phone_regex], max_length=8)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'phone_number', 'password1', 'password2']
