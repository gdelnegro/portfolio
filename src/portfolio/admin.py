from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from portfolio.models import *


@admin.register(Translation)
class TranslationAdmin(TabbedTranslationAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fields = ('image_tag', 'title', 'description',)
    readonly_fields = ('image_tag',)

@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(TabbedTranslationAdmin):
    pass

@admin.register(Frameworks)
class FrameworksAdmin(TabbedTranslationAdmin):
    pass

@admin.register(Databases)
class DatabasesAdmin(TabbedTranslationAdmin):
    pass

@admin.register(WebServers)
class WebServersAdmin(TabbedTranslationAdmin):
    pass

@admin.register(TechnologyTypes)
class TechnologyTypes(TabbedTranslationAdmin):
    pass

@admin.register(Technologies)
class TechnologiesTypes(TabbedTranslationAdmin):
    pass

@admin.register(ProjectTypes)
class ProjectTypes(TabbedTranslationAdmin):
    pass

@admin.register(Projects)
class Projects(TabbedTranslationAdmin):
    pass

@admin.register(Resume)
class Resume(TabbedTranslationAdmin):
    pass