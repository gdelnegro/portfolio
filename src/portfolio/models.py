from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from portfolio.utils.base64_image import base64_image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


TRANSLATION_TYPES_CHOICES = (
    ('MDL', _('MDL36')),
    ('TTP', _('MDL35')),
    ('MTA', _('MDL37')),
    ('MTP', _('MDL38')),
    ('GEN', _('MDL39')),
    ('GTP', _('MDL40'))
)


class TranslationType(models.Model):
    created_at = models.DateTimeField(_('MDL1'), auto_now_add=True, null=True, blank=True, help_text=_('TTP1'))
    updated_at = models.DateTimeField(_('MDL2'), auto_now=True, null=True, blank=True, help_text=_('TTP2'))
    tag = models.CharField(_('MDL32'), help_text=_('TTP32'), max_length=20, unique=True)
    name = models.TextField(_('MDL3'), help_text=_('TTP3'))
    has_auxiliary_text = models.BooleanField(_('Texto Auxiliar'), default=True)
    auxiliary_tag = models.CharField(_('MDL32'), help_text=_('TTP32'), max_length=20, unique=True)

    class Meta:
        verbose_name = _('MTA12')
        verbose_name_plural = _('MTP12')

    def __str__(self):
        return "%s - %s" % (self.tag, self.name)

    def __unicode__(self):
        return "%s - %s" % (self.tag, self.name)


class Translation(models.Model):
    created_at = models.DateTimeField(_('MDL1'), auto_now_add=True, null=True, blank=True, help_text=_('TTP1'))
    updated_at = models.DateTimeField(_('MDL2'), auto_now=True, null=True, blank=True, help_text=_('TTP2'))
    type = models.ForeignKey(TranslationType, on_delete=None, related_name="translation_translation_type",
                             verbose_name=_('MDL33'), help_text=_('TTP33'))
    tag = models.CharField(_('MDL32'), help_text=_('TTP32'), max_length=20, unique=True)
    text = models.TextField(_('MDL34'), help_text=_('TTP34'))
    auxiliary_tag = models.CharField(_('MDL42'), help_text=_('TTP42'), max_length=20, blank=True, null=True)
    auxiliary_text = models.TextField(_('MDL43'), help_text=_('TTP43'), blank=True, null=True)
    migration_created = models.BooleanField(_('Migration'), default=False)

    class Meta:
        verbose_name = _('MTA11')
        verbose_name_plural = _('MTP11')

    def __str__(self):
        return "%s" % self.tag

    def __unicode__(self):
        return "%s" % self.tag


# @receiver(post_save, sender=Translation, dispatch_uid="update_stock_count")
# def update_translation(sender, instance, **kwargs):
#     from django.core.management import call_command
#     call_command('make_translation')

class LastTranslationTag(object):
    translation_tag = None

    def __init__(self, translation_tag, *args, **kwargs):
        self.translation_tag = translation_tag

    def return_last_tag(self):
        from django.db import connection
        # query = """ SELECT max(tag) FROM portfolio_translation WHERE tag LIKE '%s%%' """ % self.translation_tag
        query = "SELECT tag FROM portfolio_translation WHERE tag LIKE '%(translation_tag)s%%' ORDER BY NULLIF(regexp_replace(TAG, E'\\\\D', '', 'g'), '')::int DESC LIMIT 1" % {
            'translation_tag': self.translation_tag}
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Exception as err:
            raise err
        else:
            result = []
            for row in cursor.fetchall():
                result = row[0]
            if result:
                import re
                tag = Translation.objects.get(tag=result)
                return dict(result=dict(last_tag=result, last_id=re.findall("(\d+)", result)[0], type=tag.type.name,
                                        has_auxiliary_text=tag.type.has_auxiliary_text,
                                        auxiliary_tag=tag.type.auxiliary_tag, tag=tag.type.tag))
            else:
                return dict(result=dict())


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('MDL1'), auto_now_add=True, null=True, blank=True, help_text=_('TTP1'))
    updated_at = models.DateTimeField(_('MDL2'), auto_now=True, null=True, blank=True, help_text=_('TTP2'))
    name = models.CharField(_('MDL3'), max_length=100, null=False, blank=False, help_text=_('TTP3'))
    description = models.TextField(_('MDL4'), null=True, blank=True, help_text=_('TTP4'))

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class Image(BaseModel):
    title = models.TextField(_('MDL49'), null=True, blank=True)
    image_string = models.TextField(_('MDL50'), null=False, blank=False)
    mimetype = models.TextField(null=False)
    extension = models.TextField(null=False)

    def image_tag(self):
        if self.mimetype:
            return u'<img src="%s" width="300px"/>' % base64_image(self.mimetype, self.image_string)
        else:
            return u'<img src="%s"  alt="placeholder" width="300px"/>' % settings.PLACEHOLDER_B64_STRING
    image_tag.short_description = _('MDL50')
    image_tag.allow_tags = True

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = _('MTA1')
        verbose_name_plural = _('MTP1')


class BaseTechnologyModel(BaseModel):
    site = models.URLField(_('MDL9'), max_length=200, null=True, blank=True, help_text=_('TTP9'))
    proficiency = models.PositiveIntegerField(_('MDL10'), help_text=_('TTP10'))
    logo = models.OneToOneField(Image, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name=_('MDL11'),
                                help_text=_('TTP11'))

    def logo_thumbnail(self):
        if self.logo:
            return u'<img src="%s" width="300px"/>' % (base64_image(self.logo.mimetype, self.logo.image_string))
        else:
            return u'<img src="%s"  alt="placeholder" width="300px"/>' % (settings.PLACEHOLDER_B64_STRING)

    logo_thumbnail.short_description = 'logo'
    logo_thumbnail.allow_tags = True

    def __str__(self):
        return "%s" % self.name

    class Meta:
        abstract = True


class ProgrammingLanguages(BaseTechnologyModel):
    class Meta:
        verbose_name = _('MTA2')
        verbose_name_plural = _('MTP2')


class Frameworks(BaseTechnologyModel):
    language = models.ForeignKey(ProgrammingLanguages, verbose_name=_('MDL12'), help_text=_('TTP12'))

    class Meta:
        verbose_name = _('MTA3')
        verbose_name_plural = _('MTP3')


class Databases(BaseTechnologyModel):
    sql = models.BooleanField(_('MDL13'), default=True, help_text=_('TTP13'))

    class Meta:
        verbose_name = _('MTA4')
        verbose_name_plural = _('MTP4')


class WebServers(BaseTechnologyModel):
    class Meta:
        verbose_name = _('MTA5')
        verbose_name_plural = _('MTP5')


class TechnologyTypes(BaseTechnologyModel):
    class Meta:
        verbose_name = _('MTA6')
        verbose_name_plural = _('MTP6')


class Technologies(BaseTechnologyModel):
    type = models.ForeignKey(TechnologyTypes, verbose_name=_('MDL14'), help_text=_('TTP14'))

    class Meta:
        verbose_name = _('MTA7')
        verbose_name_plural = _('MTP7')


class ProjectTypes(BaseModel):
    class Meta:
        verbose_name = _('MTA8')
        verbose_name_plural = _('MTP8')


class Projects(BaseModel):
    type = models.ForeignKey(ProjectTypes, verbose_name=_('MDL15'), help_text=_('TTP15'))
    programming_language = models.ManyToManyField(ProgrammingLanguages, verbose_name=_('MDL1'), help_text=_('TTP1'))
    framework = models.ManyToManyField(Frameworks, blank=True, verbose_name=_('MDL17'), help_text=_('TTP17'))
    database = models.ManyToManyField(Databases, blank=True, verbose_name=_('MDL18'), help_text=_('TTP18'))
    technology = models.ManyToManyField(Technologies, blank=True, verbose_name=_('MDL19'), help_text=_('TTP19'))
    webserver = models.ManyToManyField(WebServers, blank=True, verbose_name=_('MDL20'), help_text=_('TTP20'))
    images = models.ManyToManyField(Image, blank=True, verbose_name=_('MDL21'), help_text=_('TTP21'))

    class Meta:

        verbose_name = _('MTA9')
        verbose_name_plural = _('MTP9')


class Resume(BaseModel):
    import datetime
    EDUCATION = 'ED'
    EXPERIENCE = 'XP'
    AWARDS = 'AW'
    RESUME_TYPE_CHOICES = (
        (EDUCATION, _('MDL22')),
        (EXPERIENCE, _('MDL23')),
        (AWARDS, _('MDL24')),
    )

    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(r, r) for r in range(1, 13)]
    type = models.CharField(_('MDL25'), max_length=2, choices=RESUME_TYPE_CHOICES, default=EDUCATION,
                            help_text=_('TTP25'))
    start_month = models.PositiveIntegerField(_('MDL26'), choices=MONTH_CHOICES, default=datetime.datetime.now().month,
                                              help_text=_('TTP26')),
    start_year = models.PositiveIntegerField(_('MDL27'), choices=YEAR_CHOICES, default=datetime.datetime.now().year,
                                             help_text=_('TTP27'))
    end_month = models.PositiveIntegerField(_('MDL28'), choices=MONTH_CHOICES, default=datetime.datetime.now().month,
                                            help_text=_('TTP28')),
    end_year = models.PositiveIntegerField(_('MDL29'), choices=YEAR_CHOICES, default=datetime.datetime.now().year,
                                           help_text=_('TTP29'))
    title = models.CharField(_('MDL30'), max_length=100, null=True, help_text=_('MDL30'))
    en_title = models.CharField(_('MDL31'), max_length=100, null=True, help_text=_('MDL31'))
    where = models.TextField(_('MDL32'), null=False, help_text=_('MDL32'))

    class Meta:
        verbose_name = _('MTA10')
        verbose_name_plural = _('MTP10')


class SiteSettings(models.Model):
    created_at = models.DateTimeField(_('MDL1'), auto_now_add=True, null=True, blank=True, help_text=_('TTP1'))
    updated_at = models.DateTimeField(_('MDL2'), auto_now=True, null=True, blank=True, help_text=_('TTP2'))
    tag = models.CharField(_('MDL32'), help_text=_('TTP32'), max_length=20, unique=True)
    value = models.TextField(_('MDL34'), help_text=_('TTP34'))

    class Meta:
        verbose_name = _('MTA13')
        verbose_name_plural = _('MTP13')


CHART_TYPE_CHOICES = (
    ("bar", _('MDL39')),
    ("gauge", _('MDL40'))
)


class Skill(BaseModel):
    proficiency = models.PositiveIntegerField(_('MDL10'), help_text=_('TTP10'))
    chart_type = models.CharField(_('MDL41'), choices=CHART_TYPE_CHOICES, help_text=_('TTP41'), max_length=45)

    class Meta:
        verbose_name = _('MTA14')
        verbose_name_plural = _('MTP14')


class Keyword(models.Model):
    created_at = models.DateTimeField(_('MDL1'), auto_now_add=True, null=True, blank=True, help_text=_('TTP1'))
    updated_at = models.DateTimeField(_('MDL2'), auto_now=True, null=True, blank=True, help_text=_('TTP2'))
    tag = models.CharField(_('MDL32'), help_text=_('TTP32'), max_length=20, unique=True)
    value = models.TextField(_('MDL34'), help_text=_('TTP34'))

    class Meta:
        verbose_name = _('MTA15')
        verbose_name_plural = _('MTP15')
