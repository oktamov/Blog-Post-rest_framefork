from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import User

client = Client()


class UserRegistrationTest(TestCase):
    def test_user_register(self):
        new_user_data = {
            "email": "test2@mail.com",
            "username": 'testuser2',
            "password1": '123456',
            "password2": '123456',
        }

        url = reverse('register')
        response = client.post(url, data=new_user_data)
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        user = User.objects.create_user(
            email='test@gmail.com',
            username='testuser1',
            password='123456'
        )

        data = {
            "username_or_email": "test@gmail.com",
            "password": "123456"
        }
        url = reverse('login')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)

    def test_user_profil(self):
        self.client = APIClient()
        user = User.objects.create_user(
            email='test@gmail.com',
            username='testuser1',
            password='123456'
        )

        self.client.force_authenticate(user=user)

        url = reverse('profile')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_password_change(self):
        User.objects.create_user(
            email='tests@gmail.com',
            username='tests',
            password='123456'
        )

        data = {
            "current_password": "123456",
            "new_password": "string"
        }
        url = reverse("password-change")
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
