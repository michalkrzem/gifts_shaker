import pytest
from django.test import Client

from login.forms import CreateUserForm


def test_ligin_():
    assert 1 == 1


def test_login_correct():
    client = Client()
    response = client.get("/login/login/")

    assert response.status_code == 200


#


def test_login_incorrect_addres():
    client = Client()
    response = client.get("/login/login_incorreckt/")

    assert response.status_code == 404


def test_register_correct():
    client = Client()
    response = client.get("/login/register/")

    assert response.status_code == 200


def test_register_incorrect_addres():
    client = Client()
    response = client.get("/login/register_incorreckt/")

    assert response.status_code == 404


#
# @pytest.mark.django_db
# def test_register_user_correct():
#     # form = CreateUserForm()
#     # if request.method == 'POST':
#     form = CreateUserForm(
#         first_name='Michal',
#         last_name='Krzeminski',
#         username='mich_krem@gmail.com',
#         password1='qwe123',
#         password2='qwe123'
#     )
#     form.save()
#     user = form.cleaned_data.get('username')
#
#     assert user == 'mich_krem@gmail.com'
