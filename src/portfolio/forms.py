from django import forms
from django.utils.translation import ugettext_lazy as _
# from common.utils.file_upload import image_upload
from django.contrib.auth.models import User
from portfolio.models import *
import datetime


class UserImageAdminForm(forms.ModelForm):

    image_upload = forms.ImageField(required=False)
    user = forms.ModelChoiceField('User')

    def save(self, commit=True):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        usr = self.cleaned_data.get('user')
        username = "%s %s" % (usr.first_name, usr.last_name)
        if len(username) < 2:
            username = "%s" % (usr.username)
        filename = "%s profile picture - %s" % (username, timestamp)
        if(usr.userextend.photo_id):
            pk = usr.userextend.photo_id
        else:
            pk = None
        form_image = self.cleaned_data.get('image_upload')

        image_id, image_error = image_upload(form_image, filename, pk)
        if image_id:
            usr.userextend.photo_id = image_id
            usr.userextend.save()
        return super(UserImageAdminForm, self).save(commit=commit)

    class Meta:
        model = Image
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class OrganizationImageAdminForm(forms.ModelForm):
    image_upload = forms.ImageField(required=False)

    def save(self, commit=False):
        org = super(OrganizationImageAdminForm, self).save(commit=commit)
        org.save()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        org_name = "%s" % (org.acronym)
        filename = "%s logo - %s" % (org_name, timestamp)
        if(org.logo_id):
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