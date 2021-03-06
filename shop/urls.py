from django.urls import path
from .views import checkout, product, update_item,cart, search, ProductDetailView, filter, filter_data, wishlist, wishlist_view

app_name = 'shop'

urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='single-product'),
    path('', product, name='product'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
    path('wishlist/', wishlist, name='add_wishlist'),
    path('wishlistview/', wishlist_view, name='wishlist_view'),
    path('wishlistview/update_item/', update_item, name='update_item'),
    path('wishlistview/wishlist/', wishlist, name='add_wishlist'),
    path('cart/update_item/', update_item, name="update_item"),
    path('search/', search, name='search'),
    path('search/update_item/', update_item, name='update_item'),
    
    path('filter/<slug:slug>', filter, name='filter'),
    path('filter-data/',filter_data,name='filter_data'),


]