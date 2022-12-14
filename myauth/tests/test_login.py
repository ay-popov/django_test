from http import HTTPStatus
from random import choices
from string import ascii_lowercase, ascii_letters, digits
from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import AbstractUser

from myauth.models import UserModel


class LoginTestCase(TestCase):
    url = reverse_lazy("myauth:login")
    secret_url = reverse_lazy("myauth:secret")

    def setUp(self) -> None:
        print()
        print("Creating test User ...")
        password = "".join(choices(ascii_letters + digits, k=10))
        username = "".join(choices(ascii_lowercase, k=8))
        user: AbstractUser = UserModel.objects.create_user(
            username=username, password=password)
        self.user = user
        self.password = password

    def tearDown(self) -> None:
        print("Deleting test User ...")
        self.user.delete()

    def test_login(self):
        resp_auth = self.client.post(
            self.url,
            {
                "username": self.user.username,
                "password": self.password,
            },
        )
        self.assertEqual(resp_auth.url, reverse("myauth:me"))

        response_page = self.client.get(resp_auth.url)
        user = response_page.context["user"]
        self.assertFalse(user.is_anonymous)
        self.assertEqual(user.username, self.user.username)
        print("Testing access http://127.0.0.1:8000/auth/me/")

    def test_anon_access_to_secret_page_is_restricted(self):
        response = self.client.get(self.secret_url)
        self.assertNotEqual(response.status_code, HTTPStatus.OK)
        print("Testing access http://127.0.0.1:8000/auth/secret/")

    def test_authorised_access_to_secret_page(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.secret_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        print("Testing authorised access http://127.0.0.1:8000/auth/secret/")