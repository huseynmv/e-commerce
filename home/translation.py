from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')
    
translator.register(HomeSlider, BlogTranslationOptions)