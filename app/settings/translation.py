from modeltranslation.translator import register, TranslationOptions
from .models import KikoUpdate

@register(KikoUpdate)
class KikoUpdateTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')