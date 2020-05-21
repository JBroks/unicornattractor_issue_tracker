from django.conf.urls import url, include
from forum.views import forum, add_or_edit_thread, delete_thread, view_thread

urlpatterns = [
    url(r'^$', forum, name="forum"),
    url(r'^new/thread/$', add_or_edit_thread, name="add_thread"),
    url(r'^edit/thread/(?P<pk>\d+)/$', add_or_edit_thread, name="edit_thread"),
    url(r'^delete/thread/(?P<pk>\d+)/$', delete_thread, name="delete_thread"),
    url(r'^view/thread/(?P<pk>\d+)/$', view_thread, name="view_thread"),
]