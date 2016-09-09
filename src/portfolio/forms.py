from django import forms
from django.utils.translation import ugettext_lazy as _
from portfolio.utils.file_upload import image_upload
from django.contrib.auth.models import User
from portfolio.models import *
import datetime


class ProjectsImageAdminForm(forms.ModelForm):
    image_upload = forms.ImageField(required=False, label=_('MDL44'), help_text=_('TTP44'))

    def save(self, commit=False):
        project = super(ProjectsImageAdminForm, self).save(commit=commit)
        project.save()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = "%s image - %s" % (project.name, timestamp)
        form_image = self.cleaned_data.get('image_upload')
        image_id, image_error = image_upload(form_image, filename)
        if image_id:
            project.images.add(image_id)
            project.save()
        return project

    class Meta:
        model = Image
        fields = '__all__'


class DatabaseImageAdminForm(forms.ModelForm):
    image_upload = forms.ImageField(required=False, label=_('MDL44'), help_text=_('TTP44'))

    def save(self, commit=False):
        database = super(DatabaseImageAdminForm, self).save(commit=commit)
        database.save()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        if database.logo:
            image_pk = database.logo.id
            filename = database.logo.title
        else:
            filename = "%s logo - %s" % (database.name, timestamp)
            image_pk = None
        form_image = self.cleaned_data.get('image_upload')
        image_id, image_error = image_upload(form_image=form_image, filename=filename, pk=image_pk)
        if image_id:
            database.logo = Image.objects.get(pk=image_id)
            database.save()
        return database

    class Meta:
        model = Image
        fields = '__all__'



class TranslationAdminForm(forms.ModelForm):
    def save(self, commit=False):
        translation = super(TranslationAdminForm, self).save(commit=commit)
        translation.save()
        translation.migration_created = False
        translation.save()
        return translation

    class Meta:
        model = Translation
        fields = "__all__"