"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from accounts import urls as urls_accounts
from tickets import urls as urls_tickets
from forum import urls as urls_forum
from search import urls as urls_search
from dashboard import urls as urls_dashboard
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^tickets/', include(urls_tickets)),
    url(r'^forum/', include(urls_forum)),
    url(r'^search_results/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^dashboard/', include(urls_dashboard)),
]
