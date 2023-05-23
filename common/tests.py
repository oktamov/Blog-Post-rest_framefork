from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User


# Create your tests here.


class CategoryTest(TestCase):
    def setUp(self) -> None:
        self.cat_data = {
            'title': 'testcat1'
        }
        self.client = APIClient()

    def test_category_list(self):
        url = reverse('category-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_category_create(self):
        user = User.objects.create_superuser(
            email='test@gmail.com',
            username='testuser1',
            password='123456'
        )

        self.client.force_authenticate(user=user)

        url = reverse('category-create')
        response = self.client.post(url, data=self.cat_data)
        self.assertEqual(response.status_code, 201)
