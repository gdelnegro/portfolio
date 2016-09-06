from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from portfolio.models import *
from django.conf import settings
from portfolio.forms import *


class CustomModelAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


@admin.register(TranslationType)
class TranslationTypeAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Translation)
class TranslationAdmin(TabbedTranslationAdmin):
    fieldsets = (
        ('Translation type', {
            'fields': ('type',)
        }),
        ('Primary info', {
            'fields': ('tag', 'text')
        }),
        ('Auxiliary info', {
            'fields': ('auxiliary_tag', 'auxiliary_text')
        }),
    )
    list_display = ('tag', 'type', 'text')
    # inlines = [TranslationInline, ]

#(_('Operation'), {
#            'fields': ('installation_date', 'operation_start_date', 'status', 'operation_end_date')
#        })

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
class TechnologyTypesAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Technologies)
class TechnologiesAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(ProjectTypes)
class ProjectTypesAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Projects)
class ProjectsAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(CustomModelAdminMixin, TabbedTranslationAdmin):
    pass
