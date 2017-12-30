# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import ContactByMailForm, RegistrationDemandForm
from articles.models import Article
from events.models import Event
from .models import CustomUser

# Create your views here.


def profile_view(request, id):

    user = get_object_or_404(CustomUser, pk=id)
    articles = Article.objects.all().order_by('-id')# TODO: Get user articles
    events = Event.objects.all().order_by('-id') # TODO: Get active events
    context = {
        'user': user,
        'articles' : articles,
        'events': events
    }
    return render(request, 'user/profile.html', context)
    
