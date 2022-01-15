
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls', namespace='home')),
    path('about/',include('about.urls', namespace='about')),
    path('account/',include('account.urls', namespace='account')),
    path('blog/',include('blog.urls', namespace='blog')),
    path('contact/',include('contact.urls', namespace='contact')),
    path('pages/',include('pages.urls', namespace='pages')),
    path('shop/',include('shop.urls', namespace='shop')),
    path('vendor/',include('vendor.urls', namespace='vendor')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
