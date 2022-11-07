from django.contrib.auth.models import User
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    container = forms.CharField(
        max_length=200,
        required=False,
        help_text='Enter Group name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Container Name'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
