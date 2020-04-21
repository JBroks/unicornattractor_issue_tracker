from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, edit_profile, delete_account
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^(?P<username>\w+)/profile/$', user_profile, name="profile"),
    url(r'^(?P<username>\w+)/profile-edit/$', edit_profile, name="edit_profile"),
    url(r'^account-delete/', delete_account, name="delete_account"),
    url(r'^password-reset/', include(url_reset))
]