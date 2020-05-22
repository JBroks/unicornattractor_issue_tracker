from django.conf.urls import url, include
from forum.views import forum, add_or_edit_thread, delete_thread, view_thread, add_or_edit_post, delete_post, vote_thread

urlpatterns = [
    url(r'^$', forum, name="forum"),
    url(r'^new/thread/$', add_or_edit_thread, name="add_thread"),
    url(r'^edit/thread/(?P<pk>\d+)/$', add_or_edit_thread, name="edit_thread"),
    url(r'^delete/thread/(?P<pk>\d+)/$', delete_thread, name="delete_thread"),
    url(r'^view/thread/(?P<pk>\d+)/$', view_thread, name="view_thread"),
    url(r'^view/thread/(?P<thread_pk>\d+)/(?P<vote_type>\w+)/$', vote_thread, name="vote_thread"),
    url(r'^view/thread/(?P<thread_pk>\d+)/posts/new/$', add_or_edit_post, name="add_post"),
    url(r'^view/thread/(?P<thread_pk>\d+)/posts/edit/post/(?P<post_pk>\d+)/$', add_or_edit_post, name="edit_post"),
    url(r'^view/thread/(?P<thread_pk>\d+)/posts/delete/post/(?P<post_pk>\d+)/$', delete_post, name="delete_post")
]