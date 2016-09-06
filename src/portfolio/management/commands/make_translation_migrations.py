import django
from django.core.management import BaseCommand
from django.conf import settings
from datetime import datetime
from django.core.management import call_command
import os
import glob
from portfolio.models import Translation


class Command(BaseCommand):
    help = "This command generates migrations for translations, based on the contents of 'Translation' model"

    updated_translations = []

    migration_string = """# -*- coding: utf-8 -*-
# Generated by Django %(django_version)s on %(timestamp)s
from __future__ import unicode_literals

from django.db import migrations


def __load_data(**kwargs):
    apps = kwargs.pop('apps', None)
    translation_type = apps.get_model("portfolio", "TranslationType")
    if apps:
        model = apps.get_model("portfolio", "Translation")
        try:
            mdl = model.objects.get(tag=kwargs['tag'])
        except model.DoesNotExist:
            mdl = model()
        except Exception as err:
            raise err
        for k, v in kwargs.items():
            if k == "type":
                setattr(mdl, k, translation_type.objects.get(tag=v))
            else:
                setattr(mdl, k, v)
        setattr(mdl, "migration_created", True)
        mdl.save()


def clear_data(apps, schema_editor):
    model = apps.get_model("portfolio", "Translation")
    model.objects.filter(tag__in=[%(tags_to_remove)s]).delete()


def load_data(apps, schema_editor):
%(translation_strings)s


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '%(dependency)s'),
    ]

    operations = [
        migrations.RunPython(load_data, clear_data)
    ]

        """

    def __create_translation_lines(self):
        new_lines = []
        for translation in Translation.objects.filter(migration_created=False):
            new_lines.append(
                '    __load_data(apps=apps, tag="%(tag)s", type="%(type)s", text_pt_br="%(text_pt)s", text_en="%(text_en)s", '
                'auxiliary_tag="%(aux_tag)s", auxiliary_text_pt_br="%(aux_text_pt)s", auxiliary_text_en="%(aux_text_en)s")'
                % {
                    'tag': translation.tag,
                    'type': translation.type.tag,
                    'text_pt': translation.text_pt_br,
                    'text_en': translation.text_en,
                    'aux_tag': translation.auxiliary_tag,
                    'aux_text_pt': translation.auxiliary_text_pt_br,
                    'aux_text_en': translation.auxiliary_text_en,
                }
            )
            self.updated_translations.append(translation.tag)
        return new_lines

    def __update_translation(self):
        for tag in self.updated_translations:
            translation = Translation.objects.get(tag=tag)
            translation.migration_created = True
            translation.save()

    def __create_translation_migration(self):
        """ Create an empty migration """
        migrations_dir = settings.BASE_DIR + '/portfolio/migrations/'
        dependency_migration = os.path.basename(max(glob.iglob(migrations_dir + '*.py'), key=os.path.getctime)).replace(".py", "")
        call_command('makemigrations', 'portfolio', "--empty")
        """ Get last migration name and edit it, adding the new code """
        last_migration_file = max(glob.iglob(migrations_dir + '*.py'), key=os.path.getctime)
        new_lines = self.__create_translation_lines()
        try:
            if len(new_lines) > 0:
                with open(last_migration_file, 'w+') as file:
                    file.write(self.migration_string % {
                        'django_version': django.get_version(),
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'translation_strings': "\n".join(new_lines),
                        'dependency': dependency_migration,
                        'tags_to_remove': ",".join('"{0}"'.format(tag) for tag in self.updated_translations)
                    })
            else:
                os.remove(last_migration_file)
        except Exception as error:
            os.remove(last_migration_file)
        else:
            import subprocess
            os.chdir(migrations_dir)
            subprocess.call(["git", "add", "."])
            subprocess.call(["git", 'commit', "-m", "Added new translation migration"])
            self.__update_translation()

    def handle(self, *args, **options):
        self.__create_translation_migration()