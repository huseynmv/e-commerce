from django.urls.conf import path
from accounts import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
