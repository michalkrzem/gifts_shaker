from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory

from .models import Gifts


class CreateGift(ModelForm):
    name = forms.CharField(
        label='Nazwa prezentu'
    )
    price = forms.DecimalField(
        label='Podaj cenę'
    )

    class Meta:
        model = Gifts
        fields = ['name', 'price', 'link']
        # fields = '__all__'