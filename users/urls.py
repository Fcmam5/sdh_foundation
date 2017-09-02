from django.conf.urls import url , include
from django.contrib import admin
from .views import profile_view

urlpatterns = [
    url(r'^(?P<id>\d+)/$', view=profile_view, name='profile'),
]
