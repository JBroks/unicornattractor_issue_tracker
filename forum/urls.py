from django.conf.urls import url, include
from forum.views import forum, add_or_edit_post, delete_post, view_post

urlpatterns = [
    url(r'^$', forum, name="forum"),
    url(r'^new/post/$', add_or_edit_post, name="add_post"),
    url(r'^edit/post/(?P<pk>\d+)/$', add_or_edit_post, name="edit_post"),
    url(r'^delete/post/(?P<pk>\d+)/$', delete_post, name="delete_post"),
    url(r'^view/post/(?P<pk>\d+)/$', view_post, name="view_post"),
]