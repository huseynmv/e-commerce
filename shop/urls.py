from django.urls import path
from .views import checkout, product, update_item,cart, search, ProductDetailView, filter, filter_data, wishlist

app_name = 'shop'

urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='single-product'),
    path('', product, name='product'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
    path('wishlist/', wishlist, name='update_item'),
    path('cart/update_item/', update_item, name="update_item"),
    path('search/', search, name='search'),
    path('filter/<slug:slug>', filter, name='filter'),
    path('filter-data/',filter_data,name='filter_data'),


]