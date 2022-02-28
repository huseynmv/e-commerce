from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', faq, name='faq'),
    path('error/', error, name='error'),
    path('vendor/', vendor, name='vendor'),
    path('compare/', compare, name='compare'),
    path('order/', order, name='order'),
    path('order-view/', order_view, name='order-view'),

    
    
]