from django.contrib import admin
from forum.models import Thread, Post, ThreadVote, PostVote

# Register your models here.

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(ThreadVote)
admin.site.register(PostVote)