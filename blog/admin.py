from django.contrib import admin

from blog.models import Post, PostType

admin.site.register(PostType)
admin.site.register(Post)
