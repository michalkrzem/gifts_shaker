import json

import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

from gifts.forms import (
    CreateGift,
    CreateInvitation,
    DeleteInvitation,
    DeleteGift,
    CreateShaker,
    AddPersonToShaker,
    DeleteInvitation,
)
from gifts.models import Gift


# --------------Test Gifts--------------
@pytest.mark.django_db
def test_home_correct_address_login_user(client, login_user):
    response = client.get(reverse("home"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_home_incorrect_address(client, login_user):
    response = client.get(f'{reverse("home")}_incorrect')

    assert response.status_code == 404


# --------------Test all gifts--------------
@pytest.mark.django_db
def test_all_gifts_correct_address_login_user(client, login_user):
    response = client.get(reverse("all_gifts"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_all_gifts_incorrect_address(client, login_user):
    response = client.get(f'{reverse("all_gifts")}_incorreckt')

    assert response.status_code == 404


@pytest.mark.django_db
def test_create_gift_correct(client, login_user):
    user_model = get_user_model()

    assert user_model.objects.count() == 1
    assert user_model.objects.all()[0].id == 1

    url = reverse("new_gift")
    response = client.post(
        path=url,
        data={"name": "Desla snowboardowa", "price": 333, "link": "www.wp.pl"},
        follow=True,
    )
    assert response.status_code == 200
    assert response.redirect_chain[-1][0] == "/gifts/all_gifts"
    assert response.redirect_chain[-1][1] == 302


# @pytest.mark.django_db
# def test_create_gift_logout_user(client):
#     user_model = get_user_model()
#     url = reverse("new_gift")
#     response = client.post(
#         path=url,
#         data={
#             "name": "Desla snowboardowa",
#             "price": 333,
#             "link": "www.wp.pl"
#         },
#         follow=True
#     )
#     assert response.status_code == 300
#     assert user_model.objects.count() == 0


# @pytest.mark.django_db
# def test_delete_gift_correct_pk(client):
#     user_model = get_user_model()
#
#     assert user_model.objects.count() == 0
#
#     user_model.objects.create_user(
#         username="username@gmail.com",
#         password="zaqwsxcde123",
#     )
#     assert user_model.objects.count() == 1
#
#     form = Gift.objects.create(name="desk", price=24, link="www.wp.pl", author_id=user_model.objects.get(id=1))
#     form.save()
#     assert  Gift.objects.filter(pk=form.id).exists()
#     # assert reverse('delete_gift', args=[1]) ==2
#     url = reverse('delete_gift', kwargs={"pk": "1"})
#     response = client.delete(
#         url
#     )
#     assert response.status_code == 204
