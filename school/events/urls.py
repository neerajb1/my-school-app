from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.events, name='events'),
]
