from django.contrib import admin

from .models import HomeSlider, HomeSecondarySlider

# Register your models here.

@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    fileds = ('title_az','title_en', 'desc_az', 'desc_en', 'image',)
    
    
admin.site.register(HomeSecondarySlider)
