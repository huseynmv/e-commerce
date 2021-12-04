from django.urls.conf import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
]
