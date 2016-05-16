from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

# Create your models here.
class Image(BaseModel):
    title = models.TextField(_('Title'), null=True, blank=True)
    image_string = models.TextField(_('Image'), null=False, blank=False)
    mimetype = models.TextField(null=False)
    extension = models.TextField(null=False)
    description = models.TextField(null=True, blank=True)

    def image_tag(self):
        if self.mimetype:
            return u'<img src="%s" width="300px"/>' % (base64_image(self.mimetype, self.image_string))
        else:
            return u'<img src="%s"  alt="placeholder" width="300px"/>' % (settings.PLACEHOLDER_B64_STRING)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name_plural = _('Images')
        verbose_name = _('Image')

class BaseTechnologyModel(BaseModel):
    name = models.CharField(_('Name'), max_length=100, null=False, blank=False)
    site = models.URLField(_('Site'), max_length=200, null=False, blank=False)
    proeficiency = models.PositiveIntegerField(_('Proficiency'))
    logo = models.OneToOneField(Image, on_delete=models.CASCADE, null=True)

    def logo_thumbnail(self):
        if(self.logo):
            return u'<img src="%s" width="300px"/>' % (base64_image(self.logo.mimetype, self.logo.image_string))
        else:
            return u'<img src="%s"  alt="placeholder" width="300px"/>' % (settings.PLACEHOLDER_B64_STRING)
    logo_thumbnail.short_description = 'logo'
    logo_thumbnail.allow_tags = True

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        abstract = True

class ProgrammingLanguages(BaseTechnologyModel):
    class Meta:
        verbose_name = _("Progamming Language")
        verbose_name_plural = _("Progamming Languages")

class Frameworks(BaseTechnologyModel):
    language = models.OneToOneField(ProgrammingLanguages)
    class Meta:
        verbose_name = _("Framework")
        verbose_name_plural = _("Frameworks")

class Databases(BaseTechnologyModel):
    sql = models.BooleanField(default=True)
    class Meta:
        verbose_name = _("Database")
        verbose_name_plural = _("Databases")
    pass

class WebServers(BaseTechnologyModel):
    class Meta:
        verbose_name = _("Web server")
        verbose_name_plural = _("Web servers")

class TechnologyTypes(BaseTechnologyModel):
    class Meta:
        verbose_name = _("Technology Type")
        verbose_name_plural = _("Technology Types")

class Technologies(BaseTechnologyModel):
    type = models.OneToOneField(TechnologyTypes)
    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

class ProjectTypes(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"),null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = _("Project Type")
        verbose_name_plural = ("Project Types")

class Projects(BaseModel):
    type = models.OneToOneField(ProjectTypes)
    programming_language = models.ManyToManyField(ProgrammingLanguages)
    framework = models.ManyToManyField(Frameworks)
    database = models.ManyToManyField(Databases)
    techonology = models.ManyToManyField(Technologies)
    webserver = models.ManyToManyField(WebServers)
    description = models.TextField(_("Description"))
    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
