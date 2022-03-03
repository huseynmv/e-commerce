from django.contrib import admin
from .models import Blog, BlogCategory, Comment
from modeltranslation.translator import translator, TranslationOptions, register



# @register(Blog)
# class BlogTranslationOptions(TranslationOptions)

# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogCategory)
