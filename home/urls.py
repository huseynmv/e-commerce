from django.urls import path
from .views import index
from shop.views import *
app_name = 'home'

urlpatterns = [
    path('', index, name='home'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
    path('wishlist/', wishlist, name='add_wishlist'),
    path('wishlistview/', wishlist_view, name='wishlist_view'),
    path('wishlistview/wishlist/', wishlist, name='add_wishlist'),
    path('cart/update_item/', update_item, name="update_item"),
    
]