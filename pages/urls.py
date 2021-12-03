from django.urls.conf import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.privacy, name='privacy'),
    path('customer-service/', views.customer_service, name='customer_service'),
    path('faq/', views.faq, name='faq'),
    path('product-on-sale/', views.product_on_sale, name='product_on_sale'),
    path('policy/', views.policy, name='policy'),
    path('conditions/', views.conditions, name='conditions'),
]