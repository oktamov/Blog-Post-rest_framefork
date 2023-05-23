from django.contrib import admin
from blogs.models import Post, Comment, LikeDislike

# Register your models here.

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(LikeDislike)
