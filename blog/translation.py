from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ('name', 'desc')
    
translator.register(Blog, BlogTranslationOptions)