from django.urls import path
from .views import product,single_product

app_name = 'shop'

urlpatterns = [
    path('', product, name='product'),
    path('single-product/', single_product, name='single-product'),
]