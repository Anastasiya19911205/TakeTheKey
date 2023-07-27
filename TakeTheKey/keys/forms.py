from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class IviForm(forms.Form):
    # name_ivi = forms.CharField()
    code_ivi = forms.CharField()
    # license_ivi = forms.CharField()





