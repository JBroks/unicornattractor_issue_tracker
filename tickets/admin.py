from django.contrib import admin
from tickets.models import Ticket, Upvote, Donation
from tickets.forms import DonationForm

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Upvote)

class DonationModelAdmin(admin.ModelAdmin):
    readonly_fields=('date_created',)
    form = DonationForm