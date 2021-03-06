from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __
from django.conf import settings
from portfolio.models import *
from portfolio.serializers import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from portfolio.utils.file_upload import image_upload
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from rest_framework.permissions import AllowAny


def index(request):
    from datetime import date
    user_lang = request.META.get('HTTP_ACCEPT_LANGUAGE')
    if "pt-BR" in user_lang:
        pt_br = True
    else:
        pt_br = None

    years_of_experience = date.today().year - settings.OWNER_INFO['start_year']
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
        'gauge_skills': Skill.objects.filter(chart_type="gauge"),
        'keywords': Keyword.objects.all(),
    })


class ContactApiView(views.APIView):
    permission_classes = (AllowAny,)

    def handle(self, request, *args, **kwargs):
        if request.method == 'POST':
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            # Email the profile with the contact information
            template = get_template('portfolio/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'subject': subject,
                'message': message,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + 'Portfolio',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            try:
                email.send()
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(data=__('ME7'), status=status.HTTP_200_OK)
        else:
            return Response(data=__('ME6'), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.handle(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.handle(request, args, kwargs)


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


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)


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


def view_image_delete(request, pk=None):
    if 'img_id' in request.POST:
        _request = request.POST.copy()
        try:
            img_model = Image.objects.get(pk=_request['img_id'])
        except Image.DoesNotExist:
            return HttpResponse(status=404)
        else:
            if _request['model'] == "project":
                try:
                    project = Projects.objects.get(pk=_request['pk'])
                except Projects.DoesNotExist:
                    return HttpResponse(status=404)
                else:
                    try:
                        project.images.remove(img_model.id)
                        project.save()
                        img_model.delete()
                    except Exception as error:
                        return HttpResponse(status=500, reason=error)
                    else:
                        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


def view_image_upload(request, pk=None):
    if request.method == "POST" and request.FILES and 'img' in request.FILES and 'pk' in request.POST:
        form_image = request.FILES['img']
        _request = request.POST.copy()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if _request['model'] == "project":
            try:
                model = Projects.objects.get(pk=_request['pk'])
            except Projects.DoesNotExist:
                return HttpResponse(status=404)
            else:
                img_id = _request.get('img_id', None)
                if img_id:
                    filename = Image.objects.get(pk=img_id).title
                else:
                    filename = "%s - %s" % (model.name, timestamp)
                image_id, image_error = image_upload(form_image=form_image, filename=filename, pk=img_id)
                if image_id:
                    if img_id:
                        return HttpResponse(status=200, reason=_('ME5'))
                    else:
                        try:
                            model.images.add(image_id)
                        except Exception as error:
                            return HttpResponse(status=500, reason=error)
                        else:
                            return HttpResponse(status=200)
                else:
                    if image_error['show']:
                        return HttpResponse(status=500, reason=image_error['error_message'])
                    else:
                        return HttpResponse(status=500)

        if _request['model'] == "user":
            try:
                model = User.objects.get(pk=_request['pk'])
            except User.DoesNotExist:
                return HttpResponse(status=500, reason=_('ME17'))
            if model.userextend.photo:
                img_id = model.userextend.photo_id
                filename = model.userextend.photo
            else:
                img_id = None
            username = "%s %s" % (model.first_name, model.last_name)
            if len(username) < 2:
                username = "%s" % (model.username)
            filename = "%s profile picture - %s" % (username, timestamp)
            image_id, image_error = image_upload(form_image, filename, img_id)
            if image_id:
                try:
                    model.userextend.photo_id = image_id
                    model.userextend.save(force_update=True)
                    model.save(force_update=True)
                except Exception as error:
                    return HttpResponse(status=500, reason=error)
                else:
                    return HttpResponse(status=200)
            elif image_error['show']:
                return HttpResponse(status=500, reason=image_error["error_message"])
        else:
            return HttpResponse(status=400, reason=_('ME18'))
    else:
        return HttpResponse(status=400)