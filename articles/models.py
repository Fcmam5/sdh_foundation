# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

LANGUAGES = (
    ('ARABE','العربية'),
    ('ENGLISH','English'),
    ('FRENCH','Français'),
)

def upload_location(instance, filename):
    title = instance.post.title
    slug =  slugify(title)
    return "articles/article%s/%s" %(instance.post.id, filename)

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(CustomUser)
    title = models.CharField(_('Title'),max_length=100)
    slug = models.SlugField(_('Slug'),max_length=100, unique=True)
    description = models.TextField(_('Description'),
                help_text=_('A short description to display in search restuls'))
    body = RichTextUploadingField(_('Body'),config_name='article_body_editor')
    posted = models.DateTimeField(_('Posted'),db_index=True, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name=_('Last update'),db_index=True, auto_now_add=False, auto_now=True)
    categorie = models.ForeignKey('articles.Categorie', default=1)
    document = models.FileField(_('Document'),blank = True, null = True,
                help_text=_('Document to join in article for download'))
    language = models.CharField(_('Language'),max_length = 60,choices=LANGUAGES, default = 'ARABE')
    published = models.BooleanField(_('Published'),
                    default = False, help_text="Choose whether to publish or draft the article")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"id" : self.id})

    class Meta:
        ordering = ["-posted", "-updated"]
        verbose_name_plural = _('Articles')
        verbose_name = _('Article')

class Categorie(models.Model):
    title = models.CharField(_('Title'),max_length=100, db_index=True)
    slug = models.SlugField(_('Slug'),max_length=100, db_index=True, unique = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('categories')
        verbose_name = _('categorie')

class Images(models.Model):
    image = models.ImageField(upload_to = upload_location)
    alt_text = models.CharField(_('Image description'),max_length=100,
        help_text=_('Descripe your image, this field is important to search engines and for web accessibility'))
    post = models.ForeignKey(Article, default = None)

    class Meta:
        verbose_name_plural = _('images')
        verbose_name = _('image')
