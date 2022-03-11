from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider, HomeSecondarySlider


class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')
    
translator.register(HomeSlider, HomeSliderTranslationOptions)

class HomeSecondaySliderTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')
    
translator.register(HomeSecondarySlider, HomeSecondaySliderTranslationOptions)