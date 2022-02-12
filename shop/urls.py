from django.urls import path
from .views import checkout, product, update_item,cart, search, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('<int:pk>', ProductDetailView.as_view(), name='single-product'),
    path('', product, name='product'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
    path('cart/update_item/', update_item, name="update_item"),
    path('search/', search, name='search')
    
]