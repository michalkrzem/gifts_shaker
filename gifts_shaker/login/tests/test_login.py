import pytest
from django.test import Client
from django.contrib.auth.models import User

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


@pytest.mark.django_db
def test_register_user_client():
    client = Client()
    response = client.post(
        "/login/register/",
        {
            "username": "username@gmail.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "password1": "password",
            "password2": "password",
        },
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_register_user_user_creation_form():

    form = CreateUserForm(
        data={
            "username": "username@gmail.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "password1": "zaqwsxcde123",
            "password2": "zaqwsxcde123",
        }
    )
    form.save()
    user = User.objects.get(username="username@gmail.com")

    assert form.is_valid() == True
    assert user.username == "username@gmail.com"
