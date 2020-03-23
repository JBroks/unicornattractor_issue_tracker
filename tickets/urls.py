from django.conf.urls import url, include
from tickets.views import add_ticket, all_tickets, edit_ticket, view_ticket
#delete_ticket

urlpatterns = [
    url(r'^tickets-all/', all_tickets, name="all_tickets"),
    url(r'^ticket-add/', add_ticket, name="add_ticket"),
    url(r'^ticket-edit/', edit_ticket, name="edit_ticket"),
    url(r'^ticket-view/', view_ticket, name="view_ticket"),
    #url(r'^ticket-delete/', delete_ticket, name="delete_ticket"),
]