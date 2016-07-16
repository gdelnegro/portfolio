from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from portfolio.models import *


@admin.register(Translation)
class Translation(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fields = ('image_tag', 'title', 'description',)
    readonly_fields = ('image_tag',)

@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    pass

@admin.register(Frameworks)
class FrameworksAdmin(admin.ModelAdmin):
    pass

@admin.register(Databases)
class DatabasesAdmin(admin.ModelAdmin):
    pass

@admin.register(WebServers)
class WebServersAdmin(admin.ModelAdmin):
    pass

@admin.register(TechnologyTypes)
class TechnologyTypes(admin.ModelAdmin):
    pass

@admin.register(Technologies)
class TechnologiesTypes(admin.ModelAdmin):
    pass

@admin.register(ProjectTypes)
class ProjectTypes(admin.ModelAdmin):
    pass

@admin.register(Projects)
class Projects(admin.ModelAdmin):
    pass

@admin.register(Resume)
class Resume(admin.ModelAdmin):
    pass