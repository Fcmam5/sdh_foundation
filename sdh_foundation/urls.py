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
from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import set_language
from .views import home, about, privacy_policy, contact_us, registration_demand, errors_view
from articles.sitemaps import ArticleSitemap

sitemaps = {
    'articles' : ArticleSitemap()
}

urlpatterns = [
    # Sidi Al-houari Home Page
    url(r'^$', view=home, name='home'),

    # Sidi Al-houari About Page
    url(r'^about/', view=about, name='about'),

    # List of all articles
    url(r'^articles/', include("articles.urls")),

    # List of all events
    url(r'^events/', include("events.urls")),

    # Admin stuff TODO: Change to lOGIN
    url(r'^admin/', admin.site.urls),

    # Contact us
    url(r'^contact/', view=contact_us, name="contact_us"),

    # Privacy policy
    url(r'^privacy/', view=privacy_policy, name="privacy_policy"),

    # Registration urls
    url(r'^register/', view=registration_demand, name="register"),

    # Detail of User
    url(r'^user/', include("users.urls")),

    # For SEO
    url(r'^sitemap\.xml', sitemap, {'sitemaps': sitemaps}),
    url(r'^robots\.txt', include('robots.urls')),

    #CKEditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    #Change language
    url(r'^set_language/', set_language, name="set_language"),

]

admin.site.site_header = 'SEFoundation'
admin.site.site_title = 'SEF'
admin.site.title = "SEF"
handler400 = handler403 = handler404 = handler500 = errors_view

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
