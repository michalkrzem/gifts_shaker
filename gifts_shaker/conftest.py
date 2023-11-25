import pytest

from django.test import Client
from django.contrib.auth import get_user_model


@pytest.fixture
def client():
    client = Client(enforce_csrf_checks=False)

    return client


@pytest.mark.django_db
@pytest.fixture
def login_user(client):
    username = "username@gmail.com"
    password = "password12345"
    user_model = get_user_model()

    assert user_model.objects.count() == 0

    user_model.objects.create_user(
        username=username,
        password=password,
    )

    assert user_model.objects.count() == 1

    login_user = client.login(username=username, password=password)

    return login_user


#
