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
from .views import home
from users.views import contact_us, registration_demand

urlpatterns = [
    # Sidi Al-houari Home Page
    url(r'^$', view=home, name='home'),
    # List of all articles
    url(r'^blog/', include("articles.urls")),

    # Admin stuff
    url(r'^admin/', admin.site.urls),

    # Contact us
    url(r'^contact/', view=contact_us, name="contact_us"),
    # Registration urls
    url(r'^register/', view=registration_demand, name="registration"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
