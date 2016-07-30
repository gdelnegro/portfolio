from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from portfolio.utils import base64_image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


TRANSLATION_TYPES_CHOICES = (
    ('MDL', _('MDL036')),
    ('TTP', _('MDL035')),
    ('MTA', _('MDL037')),
    ('MTP', _('MDL038')),
    ('GEN', _('MDL039')),
    ('GTP', _('MDL040'))
)


class TranslationType(models.Model):
    created_at = models.DateTimeField(_('MDL001'), auto_now_add=True, null=True, blank=True, help_text=_('TTP001'))
    updated_at = models.DateTimeField(_('MDL002'), auto_now=True, null=True, blank=True, help_text=_('TTP002'))
    tag = models.CharField(_('MDL032'), help_text=_('TTP032'), max_length=20, unique=True)
    text = models.TextField(_('MDL034'), help_text=_('TTP034'))
    has_tooltip = models.BooleanField(_('Tooltip'), default=True)
    tooltip_tag = models.CharField(_('MDL032'), help_text=_('TTP032'), max_length=20, unique=True)

    class Meta:
        verbose_name = _('MTA020')
        verbose_name_plural = _('MTA021')

    def __str__(self):
        return "%s - %s" % (self.tag, self.text)

    def __unicode__(self):
        return "%s - %s" % (self.tag, self.text)


class Translation(models.Model):
    created_at = models.DateTimeField(_('MDL001'), auto_now_add=True, null=True, blank=True, help_text=_('TTP001'))
    updated_at = models.DateTimeField(_('MDL002'), auto_now=True, null=True, blank=True, help_text=_('TTP002'))
    type = models.ForeignKey(TranslationType, on_delete=None, related_name="translation_translation_type",
                             verbose_name=_('MDL033'), help_text=_('TTP033'))
    tag = models.CharField(_('MDL032'), help_text=_('TTP032'), max_length=20, unique=True)
    text = models.TextField(_('MDL034'), help_text=_('TTP034'))
    migration_created = models.BooleanField(_('Migration'), default=False)
    is_tooltip = models.BooleanField(_('Tooltip'), default=False)

    class Meta:
        verbose_name = _('MTA020')
        verbose_name_plural = _('MTA021')

    def __str__(self):
        return "%s" % self.tag

    def __unicode__(self):
        return "%s" % self.tag

    def last_tag(self):
        from django.db import connection
        query = """ SELECT max(tag) FROM portfolio_translation WHERE tag LIKE '%s%%' """ % self.tag[:3]
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Exception as err:
            raise err
        else:
            result = []
            for row in cursor.fetchall():
                result = row[0]
        return result


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
        query = """ SELECT max(tag) FROM portfolio_translation WHERE tag LIKE '%s%%' """ % self.translation_tag
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
                return dict(result=dict(last_tag=result, last_id=re.findall("(\d+)", result)[0]))
            else:
                return dict(result=dict())


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('MDL001'), auto_now_add=True, null=True, blank=True, help_text=_('TTP001'))
    updated_at = models.DateTimeField(_('MDL002'), auto_now=True, null=True, blank=True, help_text=_('TTP002'))
    name = models.CharField(_('MDL003'), max_length=100, null=False, blank=False, help_text=_('TTP003'))
    description = models.TextField(_('MDL004'), null=True, blank=True, help_text=_('TTP004'))

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title


class Image(BaseModel):
    title = models.TextField(_('MDL005'), null=True, blank=True, help_text=_('TTP005'))
    image_string = models.TextField(_('MDL006'), null=False, blank=False, help_text=_('TTP006'))
    mimetype = models.TextField(_('MDL007'), null=False, help_text=_('TTP007'))
    extension = models.TextField(_('MDL008'), null=False, help_text=_('TTP008'))

    def image_tag(self):
        if self.mimetype:
            return u'<img src="%s" width="300px"/>' % base64_image(self.mimetype, self.image_string)
        else:
            return u'<img src="%s"  alt="placeholder" width="300px"/>' % settings.PLACEHOLDER_B64_STRING

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = _('MTA001')
        verbose_name_plural = _('MTA002')


class BaseTechnologyModel(BaseModel):
    site = models.URLField(_('MDL009'), max_length=200, null=True, blank=True, help_text=_('TTP009'))
    proficiency = models.PositiveIntegerField(_('MDL010'), help_text=_('TTP010'))
    logo = models.OneToOneField(Image, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name=_('MDL011'),
                                help_text=_('TTP011'))

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
        verbose_name = _('MTA003')
        verbose_name_plural = _('MTA004')


class Frameworks(BaseTechnologyModel):
    language = models.ForeignKey(ProgrammingLanguages, verbose_name=_('MDL012'), help_text=_('TTP012'))

    class Meta:
        verbose_name = _('MTA005')
        verbose_name_plural = _('MTA006')


class Databases(BaseTechnologyModel):
    sql = models.BooleanField(_('MDL013'), default=True, help_text=_('TTP013'))

    class Meta:
        verbose_name = _('MTA007')
        verbose_name_plural = _('MTA008')


class WebServers(BaseTechnologyModel):
    class Meta:
        verbose_name = _('MTA009')
        verbose_name_plural = _('MTA010')


class TechnologyTypes(BaseTechnologyModel):
    class Meta:
        verbose_name = _('MTA011')
        verbose_name_plural = _('MTA012')


class Technologies(BaseTechnologyModel):
    type = models.ForeignKey(TechnologyTypes, verbose_name=_('MDL014'), help_text=_('TTP014'))

    class Meta:
        verbose_name = _('MTA013')
        verbose_name_plural = _('MTA014')


class ProjectTypes(BaseModel):
    class Meta:
        verbose_name = _('MTA015')
        verbose_name_plural = _('MTA016')


class Projects(BaseModel):
    type = models.ForeignKey(ProjectTypes, verbose_name=_('MDL015'), help_text=_('TTP015'))
    programming_language = models.ManyToManyField(ProgrammingLanguages, verbose_name=_('MDL01'), help_text=_('TTP01'))
    framework = models.ManyToManyField(Frameworks, blank=True, verbose_name=_('MDL017'), help_text=_('TTP017'))
    database = models.ManyToManyField(Databases, blank=True, verbose_name=_('MDL018'), help_text=_('TTP018'))
    technology = models.ManyToManyField(Technologies, blank=True, verbose_name=_('MDL019'), help_text=_('TTP019'))
    webserver = models.ManyToManyField(WebServers, blank=True, verbose_name=_('MDL020'), help_text=_('TTP020'))
    images = models.ManyToManyField(Image, blank=True, verbose_name=_('MDL020'), help_text=_('TTP020'))

    class Meta:
        verbose_name = _('MTA017')
        verbose_name_plural = _('MTA018')


class Resume(BaseModel):
    import datetime
    EDUCATION = 'ED'
    EXPERIENCE = 'XP'
    AWARDS = 'AW'
    RESUME_TYPE_CHOICES = (
        (EDUCATION, _('MDL022')),
        (EXPERIENCE, _('MDL023')),
        (AWARDS, _('MDL024')),
    )

    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
    MONTH_CHOICES = [(r, r) for r in range(1, 13)]
    type = models.CharField(_('MDL025'), max_length=2, choices=RESUME_TYPE_CHOICES, default=EDUCATION,
                            help_text=_('TTP025'))
    start_month = models.PositiveIntegerField(_('MDL026'), choices=MONTH_CHOICES, default=datetime.datetime.now().month,
                                              help_text=_('TTP026')),
    start_year = models.PositiveIntegerField(_('MDL027'), choices=YEAR_CHOICES, default=datetime.datetime.now().year,
                                             help_text=_('TTP027'))
    end_month = models.PositiveIntegerField(_('MDL028'), choices=MONTH_CHOICES, default=datetime.datetime.now().month,
                                            help_text=_('TTP028')),
    end_year = models.PositiveIntegerField(_('MDL029'), choices=YEAR_CHOICES, default=datetime.datetime.now().year,
                                           help_text=_('TTP029'))
    title = models.CharField(_('MDL030'), max_length=100, null=True, help_text=_('MDL030'))
    en_title = models.CharField(_('MDL031'), max_length=100, null=True, help_text=_('MDL031'))
    where = models.TextField(_('MDL032'), null=False, help_text=_('MDL032'))

    class Meta:
        verbose_name = _('MTA019')


class SiteSettings(models.Model):
    created_at = models.DateTimeField(_('MDL001'), auto_now_add=True, null=True, blank=True, help_text=_('TTP001'))
    updated_at = models.DateTimeField(_('MDL002'), auto_now=True, null=True, blank=True, help_text=_('TTP002'))
    tag = models.CharField(_('MDL032'), help_text=_('TTP032'), max_length=20, unique=True)
    value = models.TextField(_('MDL034'), help_text=_('TTP034'))

    class Meta:
        verbose_name = _('MTA022')
        verbose_name_plural = _('MTA023')
