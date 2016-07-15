from modeltranslation.translator import TranslationOptions, translator
from portfolio.models import *


class BaseModelTranslationOptions(TranslationOptions):
    "Base translation options for base model with description"
    fields = ('name', 'description')
    required_languages = ('en', 'pt-br')

# register tagged models with 'description' field for translation
translator.register(BaseModel, BaseModelTranslationOptions)
