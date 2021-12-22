from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

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
    paginate_by = 3

# def single_blog(request):
#     return render(request, 'single-blog.html')

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'single-blog.html'
    context_object_name='blog_obj'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = 'Test user'
        return context