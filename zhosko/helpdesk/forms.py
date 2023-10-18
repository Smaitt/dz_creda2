from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'phone', 'email', 'description', 'priority']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




