from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient

from blogs.models import Category, Post, Comment, LikeDislike
from users.models import User

client = Client()


class BlogTest(TestCase):
    def setUp(self) -> None:
        # self.client = APIClient()
        self.category = Category.objects.create(title='test_title')
        self.user = User.objects.create_user(
            email='tests@gmail.com',
            username='tests',
            password='123456'
        )
        self.client.login(user=self.user)
        self.post = Post.objects.create(
            title='test_title1',
            body='body',
            author=self.user,
            category=self.category
        )

        self.comment = Comment.objects.create(blog=self.post, user=self.user)

        self.post_data = {
            "title": 'test_title1',
            "body": 'body',
            "author": self.user,
            "category": self.category
        }

        self.comment_data = {
            "post": self.post,
            "content": "string"
        }

        self.like_dislike = LikeDislike.objects.create(blog=self.post, user=self.user, type='1')
        self.like_dislike_data = {
                "type": -1
        }

    def test_post_list(self):
        url = reverse('post_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        url = reverse('post_create')
        response = self.client.post(url, data=self.post_data)

        self.assertEqual(response.status_code, 201)

    def test_post_detail(self):
        url = reverse('post_detail', kwargs={'slug': self.post.slug})
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_post_liked(self):
        url = reverse('post_likes', kwargs={'slug': self.post.slug})
        response = client.post(url, data=self.like_dislike_data)

        self.assertEqual(response.status_code, 201)

    def test_comment_get(self):
        self.client.login(user=self.user)
        url = reverse('comment_list_create', kwargs={'slug': self.post.slug})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_comment_create(self):
        url = reverse('comment_list_create', kwargs={'slug': self.post.slug})
        response = self.client.post(url, data=self.comment_data)

        self.assertEqual(response.status_code, 201)
