from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import index, event_detail
#TODO Fix Event urls

urlpatterns = [
    # List of all articles
    url(r'^$', view=index, name='events'),
    # Detail of an event
    url(r'^(?P<id>\d+)/$', view=event_detail, name='event'),
  ]
