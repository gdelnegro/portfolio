from django import forms
from django.utils.translation import ugettext_lazy as _
from portfolio.utils.file_upload import image_upload
from django.contrib.auth.models import User
from portfolio.models import *
import datetime


class ProjectsImageAdminForm(forms.ModelForm):
    image_upload = forms.ImageField(required=False, label=_('LB222'), help_text=_('TP222'))

    def save(self, commit=False):
        org = super(ProjectsImageAdminForm, self).save(commit=commit)
        org.save()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        org_name = "%s" % org.acronym
        filename = "%s logo - %s" % (org_name, timestamp)
        if org.logo_id:
            pk = org.logo_id
        else:
            pk = None
        form_image = self.cleaned_data.get('image_upload')
        image_id, image_error = image_upload(form_image, filename, pk)
        if image_id:
            org.logo_id = image_id
            org.save()
        return org

    class Meta:
        model = Image
        fields = '__all__'
        widgets = {'organization': forms.HiddenInput()}


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