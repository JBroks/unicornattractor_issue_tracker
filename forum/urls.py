from django.conf.urls import url, include
from .views import add_or_edit_post, forum

urlpatterns = [
    url(r'^$', forum, name="forum"),
    url(r'^new/post/$', add_or_edit_post, name="add_post"),
    url(r'^edit/post/(?P<pk>\d+)/$', add_or_edit_post, name="edit_post"),
]