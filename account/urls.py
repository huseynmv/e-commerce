from django.urls import path, re_path
from .views import login,my_account,register, activate,logout

app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('my-account/', my_account, name='my-account'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]