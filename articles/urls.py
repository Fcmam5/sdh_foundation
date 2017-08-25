from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import index, post_create, post_detail, post_update, post_delete, post_search

urlpatterns = [
    # List of all articles
    url(r'^$', view=index, name='articles'),

    # Create an article
    url(r'^create/$', view=post_create, name='create'),

    # Detail of an article
    url(r'^(?P<id>\d+)/$', view=post_detail, name='detail'),

    # Update an article
    url(r'^update/(?P<id>\d+)/$', view=post_update, name='update'),

    # Delete an article
    url(r'^delete/(?P<id>\d+)$', view=post_delete, name='delete'),

    #Search engine
    url(r'^search/$', view= post_search, name='post_search'),
  ]
