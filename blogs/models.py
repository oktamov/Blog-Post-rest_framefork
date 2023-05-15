import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.title)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    image = models.ImageField('images', null=True, blank=True)
    video = models.FileField('video', null=True, blank=True)
    tag = models.ForeignKey(Tag, related_name='tag', on_delete=models.CASCADE)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    views = models.IntegerField(default=0)
    pub_year = datetime.datetime.now().strftime("%H:%M / %d.%m.%Y")

    # comment = models.ManyToManyField('Comment', related_name='comments', blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    @property
    def num_likes(self):
        return self.liked.all().count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
