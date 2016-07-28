from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from portfolio.models import *
from django.conf import settings


class CustomModelAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


@admin.register(TranslationType)
class TranslationTypeAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Translation)
class TranslationAdmin(TabbedTranslationAdmin):
    list_display = ('tag', 'type', 'text', 'type')
    fields = ('last_tag', 'type', 'tag', 'text')
    readonly_fields = ('last_tag', )

    class Media:
        import os
        js_dir = os.path.join(settings.STATIC_URL, 'admin/js')
        js = (
            js_dir + '/admin-translation.js',
        )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fields = ('image_tag', 'title', 'description',)
    readonly_fields = ('image_tag',)


@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Frameworks)
class FrameworksAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Databases)
class DatabasesAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(WebServers)
class WebServersAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(TechnologyTypes)
class TechnologyTypes(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Technologies)
class TechnologiesTypes(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(ProjectTypes)
class ProjectTypes(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Projects)
class Projects(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Resume)
class Resume(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettings(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass