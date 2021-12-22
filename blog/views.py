from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView

# class BlogListView(ListView):
#     pass

# Create your views here.
# def blog(request):
#     blog = Blog.objects.all()
#     context = {
#         'blog' : blog
#     }
#     return render(request, 'blog.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 2

def single_blog(request):
    return render(request, 'single-blog.html')