from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

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


class AddPersonToShaker(ModelForm):
    user = forms.EmailField(
        label='Wpisz email'
    )

    class Meta:
        model = User
        fields = ['username']
