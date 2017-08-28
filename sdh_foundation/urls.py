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
from django.contrib.sitemaps.views import sitemap
from .views import home, about, profile
from users.views import contact_us, registration_demand
from articles.sitemaps import ArticleSitemap

sitemaps = {
    'articles' : ArticleSitemap()
}

urlpatterns = [
    # Sidi Al-houari Home Page
    url(r'^$', view=home, name='home'),

    # Sidi Al-houari Home Page
    url(r'^about/', view=about, name='about'),

    # List of all articles
    url(r'^articles/', include("articles.urls")),

    # List of all events
    url(r'^events/', include("events.urls")),

    # User profile
    url(r'^profile/', view=profile, name='profile'),

    # Admin stuff TODO: Change to lOGIN
    url(r'^admin/', admin.site.urls),

    # Contact us
    url(r'^contact/', view=contact_us, name="contact_us"),

    # Registration urls
    url(r'^register/', view=registration_demand, name="register"),

    # For SEO
    url(r'^sitemap\.xml', sitemap, {'sitemaps': sitemaps}),
    url(r'^robots\.txt', include('robots.urls')),
]

admin.site.site_header = 'SEFoundation'
admin.site.site_title = 'SEF'
admin.site.title = "SEF"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
