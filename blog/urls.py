from django.urls import path
from .views import blog, single_blog

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-details/', single_blog, name='blog-details'),
]