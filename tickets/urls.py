from django.conf.urls import url, include
from tickets.views import add_or_edit_ticket, all_tickets, view_ticket, delete_ticket, upvote, downvote

urlpatterns = [
    url(r'^tickets-all/', all_tickets, name="all_tickets"),
    url(r'^new/$', add_or_edit_ticket, name="add_ticket"),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_ticket, name="edit_ticket"),
    url(r'^(?P<pk>\d+)/view/$', view_ticket, name="view_ticket"),
    url(r'^(?P<pk>\d+)/ticket-delete/$', delete_ticket, name="delete_ticket"),
    url(r'^(?P<pk>\d+)/upvote/$', upvote, name="upvote"),
    url(r'^(?P<pk>\d+)/downvote/$', downvote, name="downvote")
]