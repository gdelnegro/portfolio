from django.core.management import BaseCommand
from django.conf import settings
from datetime import datetime
from portfolio.models import Translation
from django.core.management import call_command


class Command(BaseCommand):
    help = "This command executes all steps for translation"

    def handle(self, *args, **options):
        call_command('make_translation_migrations')
        call_command('migrate', 'portfolio')
        call_command('make_translation')