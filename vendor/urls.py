from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', vendor , name='vendor'),
    path('single-vendor/', single_vendor ,name='single-vendor'),
]