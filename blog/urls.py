from django.urls import path
from .views import  BlogDetailView, BlogListView, dump_database_view

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog-details'),
    path('dump-database', dump_database_view, name='dump'),
]