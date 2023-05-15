
from django.test import TestCase, Client
from users.models import User
from django.urls import reverse

client = Client()


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='mail@gmail.com',
            username='mail',
            password='1',
            password2='1'
        )

    def test_user_list(self):
        url = reverse("register")

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["email"], self.user.email)#         }