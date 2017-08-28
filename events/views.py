# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from events.models import Event
# Create your views here.
def index(request):
    events = Event.objects.all().order_by('-timing')
    today = timezone.now().date()
    paginator = Paginator(events, 5) # Show 5 contacts per page
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
    'events' : events,
    'today' : today,
    'paginator': queryset,
    'page_request_variable' : page_request_variable
    }
    return render(request, 'events.html', context)
