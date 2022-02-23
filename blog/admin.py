from django.contrib import admin
from .models import Blog, BlogCategory, Comment, BlogTag
# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogTag)
admin.site.register(Comment)
admin.site.register(BlogCategory)
