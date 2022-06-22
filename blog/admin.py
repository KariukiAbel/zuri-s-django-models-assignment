from blog.models import Post
from django.contrib import admin
from .models import Post, BlogModel

# Register your models here.
admin.site.register(BlogModel)
# admin.site.register(Post)