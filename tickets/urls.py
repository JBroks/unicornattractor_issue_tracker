from django.conf.urls import url, include
from tickets.views import add_or_edit_ticket, all_tickets, view_ticket, delete_ticket, upvote, downvote, add_or_edit_comment, delete_comment

urlpatterns = [
    url(r'^$', all_tickets, name="all_tickets"),
    url(r'^new/$', add_or_edit_ticket, name="add_ticket"),
    url(r'^edit/ticket/(?P<pk>\d+)/$', add_or_edit_ticket, name="edit_ticket"),
    url(r'^delete/ticket/(?P<pk>\d+)/$', delete_ticket, name="delete_ticket"),
    url(r'^upvote/ticket/(?P<pk>\d+)/$', upvote, name="upvote"),
    url(r'^downvote/ticket/(?P<pk>\d+)/$', downvote, name="downvote"),
    url(r'^view/ticket/(?P<pk>\d+)/$', view_ticket, name="view_ticket"),
    url(r'^view/ticket/(?P<ticket_pk>\d+)/comments/new/$', add_or_edit_comment, name="add_comment"),
    url(r'^view/ticket/(?P<ticket_pk>\d+)/comments/edit/(?P<pk>\d+)/$', add_or_edit_comment, name="edit_comment"),
    url(r'^view/ticket/(?P<ticket_pk>\d+)/comments/delete/(?P<pk>\d+)/$', delete_comment, name="delete_comment")
]