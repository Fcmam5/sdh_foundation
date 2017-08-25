from django.contrib.sitemaps import Sitemap

from .models import Article

class ArticleSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Article.objects.all()
