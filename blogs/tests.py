from django.test import TestCase, Client
from django.urls import reverse

from blogs.models import Tag, Post
from users.models import User

client = Client()


class TestPost(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(title="Newtag1")
        author = User.objects.create(username="Newuser")
        self.post = Post.objects.create(
            title="New product2",
            body='1000',
            tag=self.tag,
            author=author,
        )
        self.data = {
            "title": "new product2",
            "body": '1000',
            "tag": self.tag.id,
            "author": author.id
        }

    def test_post_list(self):
        url = reverse("post_list")

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["title"], self.post.title)

    def test_post_create(self):
        url = reverse("post_create")

        response = client.post(url, data=self.data)

        self.assertEqual(response.status_code, 201)
        # self.assertNotEqual(response.status_code, 400)
        # self.assertEqual(response.data["title"], self.data["title"])

    def test_post_detail(self):
        url = reverse("post_detail")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
