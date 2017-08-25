"""shagram URL Configuration

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
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about
from users.views import contact_us, registration_demand

urlpatterns = [
    # Sidi Al-houari Home Page
    url(r'^$', view=home, name='home'),

    # Sidi Al-houari Home Page
    url(r'^about/', view=about, name='about'),

    # List of all articles
    url(r'^articles/', include("articles.urls")),

    # List of all events
    url(r'^events/', include("events.urls")),

    # Admin stuff TODO: Change to lOGIN
    url(r'^admin/', admin.site.urls),

    # Contact us
    url(r'^contact/', view=contact_us, name="contact_us"),

    # Registration urls
    url(r'^register/', view=registration_demand, name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
