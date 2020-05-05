from django.conf.urls import url, include
from tickets.views import add_or_edit_ticket, all_tickets, view_ticket, delete_ticket, upvote, downvote, add_or_edit_comment

urlpatterns = [
    url(r'^tickets-all/', all_tickets, name="all_tickets"),
    url(r'^new/$', add_or_edit_ticket, name="add_ticket"),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_ticket, name="edit_ticket"),
    url(r'^view_ticket/(?P<pk>\d+)/$', view_ticket, name="view_ticket"),
    url(r'^ticket-delete/(?P<pk>\d+)/$', delete_ticket, name="delete_ticket"),
    url(r'^upvote/(?P<pk>\d+)/$', upvote, name="upvote"),
    url(r'^downvote/(?P<pk>\d+)/$', downvote, name="downvote"),
    url(r'^edit_comment/(?P<pk>\d+)/$', add_or_edit_comment, name="edit_comment"),
    url(r'^new_comment/$', add_or_edit_comment, name="add_comment")
]