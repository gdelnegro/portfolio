from modeltranslation.translator import TranslationOptions, translator
from portfolio.models import *


class BaseModelTranslationOptions(TranslationOptions):
    "Base translation options for base model with description"
    fields = ('name', 'description')
    required_languages = ('en', 'pt-br')


class TranslationModelTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('en', 'pt-br')


class SiteSettingsModelTranslationOptions(TranslationOptions):
    fields = ('value',)
    required_languages = ('en', 'pt-br')

translator.register(BaseModel, BaseModelTranslationOptions)
translator.register(Translation, TranslationModelTranslationOptions)
translator.register(TranslationType, TranslationModelTranslationOptions)
translator.register(ProgrammingLanguages, BaseModelTranslationOptions)
translator.register(Frameworks, BaseModelTranslationOptions)
translator.register(Databases, BaseModelTranslationOptions)
translator.register(WebServers, BaseModelTranslationOptions)
translator.register(TechnologyTypes, BaseModelTranslationOptions)
translator.register(Technologies, BaseModelTranslationOptions)
translator.register(ProjectTypes, BaseModelTranslationOptions)
translator.register(Projects, BaseModelTranslationOptions)
translator.register(Resume, BaseModelTranslationOptions)
translator.register(SiteSettings, SiteSettingsModelTranslationOptions)
