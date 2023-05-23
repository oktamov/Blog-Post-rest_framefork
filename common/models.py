from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.title)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)
