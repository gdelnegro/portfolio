from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render_to_response('portfolio/index.html', locals())
    return render(request, 'portfolio/index.html', {"appActive": "common", "pageActive": "dashboard-main", "sidebarActive": "dashboard", 'settings': settings})
