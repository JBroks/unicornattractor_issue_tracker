from django.contrib import admin
from tickets.models import Ticket, Upvote, Donation, Comment

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Upvote)
admin.site.register(Donation)
admin.site.register(Comment)
