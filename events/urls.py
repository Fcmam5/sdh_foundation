from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import index
#TODO Fix Event urls

urlpatterns = [
    # List of all articles
    url(r'^$', view=index, name='events'),
  ]
