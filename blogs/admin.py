from django.contrib import admin
from blogs.models import Tag, Post

# Register your models here.

admin.site.register(Tag)
# admin.site.register(Comment)
admin.site.register(Post)
