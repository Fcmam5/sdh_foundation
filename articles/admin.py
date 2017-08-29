# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Categorie, Images
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _

def publish_posts(modeladmin, request, queryset):
    queryset.update(published=True)
publish_posts.short_description = _("Publish selected posts")

def unpublish_posts(modeladmin, request, queryset):
    queryset.update(published=False)
unpublish_posts.short_description = _("Unpublish selected posts")


# Register your models here.
class ProjectImageAdmin(admin.ModelAdmin):
    pass

class ProjectImageInline(admin.StackedInline):
    model = Images
    max_num=10
    extra=0


class BlogAdmin(admin.ModelAdmin):
    exclude = ['author']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'updated', 'posted', 'author','published']
    list_display_link = ['title']
    list_filter = ['categorie', 'posted', 'updated']
    inlines  = [ProjectImageInline,]
    actions = [publish_posts, unpublish_posts]
    class Meta:
        model = Article
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Article, BlogAdmin)
admin.site.register(Categorie, CategoryAdmin)
