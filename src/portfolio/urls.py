"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from portfolio.views import *
from rest_framework import routers
from django.http import HttpResponse

router = routers.DefaultRouter()
router.register(r'translation', TranslationViewSet)
router.register(r'translation_type', TranslationTypeViewSet)
router.register(r'project', ProjectViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/last_translation_tag/(?P<tag>\w+)[/]?$', LastTranslationTagView.as_view(), name='get_last_translation_tag'),
    url(r'^delete_image/$', view_image_delete, name="view_image_delete"),
    url(r'^delete_image/(?P<pk>[0-9]+)/$', view_image_delete, name="view_image_delete"),
    url(r'^upload_image/$', view_image_upload, name="view_image_upload"),
    url(r'^upload_image/(?P<pk>[0-9]+)/$', view_image_upload, name="view_image_upload"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', contact, name='contact'),
    url(r'^$', index, name='index'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"),
        name="robots_file"),
]

#urlpatterns = i18n_patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', views.index, name='index'),
#    # ...
#)
