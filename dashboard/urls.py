from django.conf.urls import url, include
from dashboard.views import dashboard

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
]
