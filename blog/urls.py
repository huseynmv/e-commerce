from django.urls import path
from .views import  single_blog, BlogListView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('blog-details/', single_blog, name='blog-details'),
]