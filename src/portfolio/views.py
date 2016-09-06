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
        'bar_skills': Skill.objects.filter(chart_type="bar"),
        'gauge_skills': Skill.objects.filter(chart_type="gauge")
    })


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'tag', 'type')


class TranslationTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TranslationType.objects.all()
    serializer_class = TranslationTypeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'tag')


class LastTranslationTagView(views.APIView):
    def get(self, request, *args, **kwargs):
        if len(kwargs['tag']) > 0:
            try:
                int(kwargs['tag'])
            except ValueError:
                try:
                    model = TranslationType.objects.get(tag=kwargs['tag'])
                except TranslationType.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    model = TranslationType.objects.get(pk=kwargs['tag'])
                except TranslationType.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            last_translation_tag = LastTranslationTag(model.tag, *args, **kwargs)
            result = last_translation_tag.return_last_tag()
        else:
            result = dict(result=dict())
        return Response(result, status=status.HTTP_200_OK)