from django.urls.conf import path
from product import views

app_name = 'product'

urlpatterns = [
    path('checkout/', views.checkout, name='views-checkout'),
    path('order-tracking/', views.order_tracking, name='order-tracking'),
    path('', views.shop, name='shop'),
    path('single-views/', views.single_product, name='single-views'),
]