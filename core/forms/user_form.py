from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from core.models import User
from django.forms import ModelForm, widgets


class Create_Account_Form(UserCreationForm):
    email = forms.EmailField
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,10}$', message='Phone number')
    Phone_Number = forms.CharField(validators=[phone_regex], max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'Phone_Number', 'password1', 'password2']
        help_texts = {
            'password2': None,
            'username': None,
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id',
                   'password',
                   'last_login',
                   'is_superuser',
                   'groups',
                   'user_permissions',
                   'username',
                   'is_staff',
                   'is_active',
                   'date_joined'
                   ]
        widgets = {
            'Phone_Number': widgets.TextInput(attrs={'class': 'form-control'}),
            'Profile_Image': widgets.TextInput(attrs={'class': 'form-control'}),
            'Street_Name': widgets.TextInput(attrs={'class': 'form-control'}),
            'House_Number': widgets.TextInput(attrs={'class': 'form-control'}),
            'Country': widgets.Select(attrs={'class': 'form-control'}),
            'Postal_Code': widgets.TextInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'})
        }
