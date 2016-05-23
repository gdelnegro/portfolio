from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from portfolio import settings


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
    site = models.URLField(_('Site'), max_length=200, null=True, blank=True)
    proeficiency = models.PositiveIntegerField(_('Proficiency'))
    logo = models.OneToOneField(Image, on_delete=models.DO_NOTHING, null=True, blank=True)

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
    type = models.ForeignKey(TechnologyTypes)
    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

class ProjectTypes(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"),null=True, blank=True)
    en_name = models.CharField(_("En Name"), max_length=100, null=True)
    en_description = models.TextField(_("En Description"),null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = _("Project Type")
        verbose_name_plural = ("Project Types")

class Projects(BaseModel):
    type = models.OneToOneField(ProjectTypes)
    name = models.CharField(_("Project Name"), max_length=100, null=True)
    en_name = models.CharField(_("En Project Name"), max_length=100, null=True)
    programming_language = models.ManyToManyField(ProgrammingLanguages)
    framework = models.ManyToManyField(Frameworks, null=True, blank=True)
    database = models.ManyToManyField(Databases, null=True, blank=True)
    techonology = models.ManyToManyField(Technologies, null=True, blank=True)
    webserver = models.ManyToManyField(WebServers, null=True, blank=True)
    description = models.TextField(_("Description"), null=True)
    en_description = models.TextField(_("En Description"), null=True)
    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

class Resume(BaseModel):
    import datetime
    EDUCATION = 'ED'
    EXPERIENCE = 'XP'
    AWARDS = 'AW'
    RESUME_TYPE_CHOICES = (
        (EDUCATION, _("Education")),
        (EXPERIENCE, _("Experience")),
        (AWARDS, _("Awards")),
    )

    YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]

    type = models.CharField(max_length=2,
                            choices=RESUME_TYPE_CHOICES,
                            default=EDUCATION)
    start_year = models.IntegerField(_('start year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    end_year = models.IntegerField(_('end year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    title = models.CharField(_("Title"), max_length=100, null=True)
    en_title = models.CharField(_("En Title"), max_length=100, null=True)
    description = models.TextField(_("Description"), null=True)
    en_description = models.TextField(_("En Description"), null=True)
    where = models.TextField(_("Where"), null=False)

    class Meta:
        verbose_name = _("Resume")

    def __str__(self):
        return "%s" % (self.title)
