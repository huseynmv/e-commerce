from django.urls.conf import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
]
