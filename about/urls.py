from django.urls.conf import path
from about import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
]
