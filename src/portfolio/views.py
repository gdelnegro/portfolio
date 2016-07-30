from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from portfolio.models import *
from portfolio.serializers import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status


def index(request):
    from datetime import date
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


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'tag', 'type')


class LastTranslationTagView(views.APIView):
    def get(self, request, *args, **kwargs):
        if len(kwargs['tag']) > 0:
            myClass = LastTranslationTag(kwargs['tag'], *args, **kwargs)
            result = myClass.return_last_tag()
        else:
            result = dict(result=dict())
        return Response(result, status=status.HTTP_200_OK)
