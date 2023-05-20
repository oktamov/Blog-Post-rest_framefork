from django.test import TestCase, Client
from django.urls import reverse

from users.models import User

client = Client()


class MyTest(TestCase):
    def test_sum(self):
        result = 2 + 2
        self.assertEqual(result, 4)


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


# def test_user_registration(self):
#     # Test uchun kerakli malumotlarni tayyorlash
#     email = 'test@gmail.com'
#     username = 'testuser'
#     password = 'testpassword'
#
#     # Userni ro'yhatga olish
#     User.objects.create_user(email=email, username=username, password=password)
#
#     # Ro'yhatdan o'tgan userlarni tekshirish
#     user = User.objects.get(username=username)
#     self.assertEqual(user.username, username)
#     self.assertTrue(user.check_password(password))
#     # Boshqa user atributlarini tekshirishingiz mumkin
#
#     # Ro'yhatdan o'tmagan username uchun tekshirish
#     non_existent_user = User.objects.filter(username='nonexistentuser').exists()
#     self.assertFalse(non_existent_user)
