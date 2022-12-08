from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory

from .models import Gift, Invitation, Shaker


class CreateGift(ModelForm):
    name = forms.CharField(
        label='Nazwa prezentu'
    )
    price = forms.DecimalField(
        label='Podaj cenę'
    )

    class Meta:
        model = Gift
        fields = ['name', 'price', 'link']
        # fields = '__all__'


class DeleteGift(ModelForm):

    class Meta:
        model = Gift
        fields = ['name', 'price', 'link']


class CreateInvitation(ModelForm):
    email = forms.EmailField(
        label='Wpisz email'
    )

    class Meta:
        model = Invitation
        fields = ['email']


class DeleteInvitation(ModelForm):

    class Meta:
        model = Invitation
        fields = ['email', 'accepted']


class CreateShaker(ModelForm):

    class Meta:
        model = Shaker
        fields = ['shaker_name']
