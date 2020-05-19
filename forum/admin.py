from django.contrib import admin
from forum.models import Post, CommentPost

# Register your models here.

admin.site.register(Post)
admin.site.register(CommentPost)