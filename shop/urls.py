from django.urls import path
from .views import checkout, product,single_product, update_item,cart

app_name = 'shop'

urlpatterns = [
    path('', product, name='product'),
    path('single-product/', single_product, name='single-product'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
    path('cart/update_item/', update_item, name="update_item"),
    
]