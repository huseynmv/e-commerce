from django.urls import path
from .views import product,single_product, update_item

app_name = 'shop'

urlpatterns = [
    path('', product, name='product'),
    path('update_item', update_item, name='update_item'),
    path('single-product/', single_product, name='single-product'),
]