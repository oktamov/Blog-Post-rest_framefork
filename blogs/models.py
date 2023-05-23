import datetime

from django.db import models
from django.utils.text import slugify

from common.models import Category
from users.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)
    views = models.BigIntegerField(default=0, blank=True)
    pub_year = datetime.datetime.now().strftime("%H:%M / %d.%m.%Y")

    # comment = models.ManyToManyField('Comment', related_name='comments', blank=True)

    def __str__(self):
        return str(self.title)

    @property
    def likes(self):
        return self.like_dislikes.filter(type=LikeDislike.LikeType.LIKE).count()

    @property
    def dislikes(self):
        return self.like_dislikes.filter(type=LikeDislike.LikeType.DISLIKE).count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)


class LikeDislike(models.Model):
    class LikeType(models.IntegerChoices):
        DISLIKE = -1
        LIKE = 1

    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_dislikes")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="like_dislikes")
    type = models.SmallIntegerField(choices=LikeType.choices)

    class Meta:
        unique_together = ["blog", "user"]

    def __str__(self):
        return f"{self.user}"


class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=200)
    parent = models.ForeignKey("self", models.CASCADE, related_name="replies", null=True)

    def __str__(self):
        return self.body
