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
    exclude = ['author', 'published']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'updated', 'author','language','published']
    list_display_link = ['title']
    list_filter = ['categorie', 'posted', 'updated', 'language']
    inlines  = [ProjectImageInline,]
    actions = [publish_posts, unpublish_posts]
    search_fields = ['title', 'body', 'description']
    class Meta:
        model = Article
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        """
        Scientist can only see his articles.
        Staffs and superuser can see articles of any author(scientist)
        """
        qs = super(BlogAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.account_type == 2:
            return qs
        return qs.filter(author=request.user)

    def get_actions(self, request):
        """
        Show Publish/Unpublish actions only for staffs and superuser
        """
        actions = super(BlogAdmin, self).get_actions(request)
        if request.user.account_type == 1 and not request.user.is_superuser:
            del actions['publish_posts']
            del actions['unpublish_posts']
        return actions

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Article, BlogAdmin)
admin.site.register(Categorie, CategoryAdmin)
