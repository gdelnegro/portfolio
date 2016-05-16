from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from portfolio.models import *

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render_to_response('portfolio/index.html', locals())
    user_lang = request.META.get('HTTP_ACCEPT_LANGUAGE')
    if "pt-BR" in user_lang:
        user_lang = True
    else:
        user_lang = None        
    return render(request, 'portfolio/index.html', {
        "appActive": "portfolio",
        'settings': settings,
        'projects': Projects.objects.all(),
        'projects_types': ProjectTypes.objects.all(),
        'user_lang': user_lang
        })
