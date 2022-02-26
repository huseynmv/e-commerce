from django.urls import path
from .views import  BlogDetailView, BlogListView, dump_database_view, blog_search, TagIndexView, blog_filter

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<slug:slug>', BlogDetailView.as_view(), name='blog-details'),
    path('dump-database', dump_database_view, name='dump'),
    path('search-blog/', blog_search, name='blog-search'),
    path('blog-filter/<slug:slug>', blog_filter, name='blog-filter'),
    path('tags/<slug:tag_slug>/',TagIndexView.as_view(), name='posts_by_tag'), 
    
]