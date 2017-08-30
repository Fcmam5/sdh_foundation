# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

# Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Search
from haystack.query import SearchQuerySet
from articles.forms import SearchForm

from articles.models import Article, Categorie, Images
from events.models import Event

from .forms import PostForm, ImageForm
# Display all categories and all posts

@csrf_protect
def index(request):
    posts = Article.objects.filter(published=True).order_by('-posted')
    categories = Categorie.objects.all().order_by('-id')
    events = Event.objects.all().order_by('-id')
    today = timezone.now().date()
    paginator = Paginator(posts, 2) # Show 2 contacts per page
    page_request_variable = 'page'
    page = request.GET.get(page_request_variable)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'posts' : posts,
        'events' : events,
        'today' : today,
        'paginator': queryset,
        'page_request_variable' : page_request_variable
    }
    return render(request, 'articles/articles_list.html', context)

# Create Post
@csrf_protect
def post_create(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=1)
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Yeeew,check it out on the home page!")
            return HttpResponseRedirect("/blog")
        else:
            print postForm.errors, formset.errors
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context_instance=RequestContext(request)
    return render(request, 'post_form.html',
                  {
                      'postForm': postForm,
                      'formset': formset,
                      'context_instance' : context_instance
                      })

# Display the post
@csrf_protect
def post_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    events = Event.objects.all().order_by('-id')
    images = Images.objects.all().order_by('-id')
    today = timezone.now().date()
    context ={
        'article' : article,
        'events' : events,
        'today' : today,
        'images' : images
    }
    return render(request, 'article.html', context)
# Display the first 2 posts in a specefic category

# Create Post
@csrf_protect
def post_update(request, id):
    return HttpResponse("<h1>Update POST "+id+" </h1>")

# Create Post
@csrf_protect
def post_delete(request, id):
    return HttpResponse("<h1>Delete POST "+id+" </h1>")

# Search view
@csrf_protect
def post_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Article).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
        else:
            cd = ''
            results = ""
            total_results = 0
    else:
        cd = ''
        results = ""
        total_results = 0
    return render(request,
                  'articles/articles_search.html',
                  {'form': form,
                   'cd': cd,
                   'results': results,
                   'total_results': total_results})
