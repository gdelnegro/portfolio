from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from portfolio.models import *

def index(request):
    from datetime import date
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render_to_response('portfolio/index.html', locals())
    user_lang = request.META.get('HTTP_ACCEPT_LANGUAGE')
    if "pt-BR" in user_lang:
        pt_br = True
    else:
        pt_br = None

    years_of_experience = date.today().year - 2008
    return render(request, 'portfolio/index.html', {
        "appActive": "portfolio",
        'settings': settings,
        'projects': Projects.objects.all(),
        'projects_types': ProjectTypes.objects.all(),
        'pt_br': pt_br,
        'resume_education': Resume.objects.filter(type="ED"),
        'resume_experiences': Resume.objects.filter(type="XP"),
        'years': years_of_experience,
        })
