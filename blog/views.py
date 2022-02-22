
from gc import get_objects
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Blog
from django.views.generic import ListView, DetailView
from . tasks import dump_database
from .forms import BlogCommentForm

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
    
     
    form = BlogCommentForm
    
    def post(self, request, *args, **kwargs):
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return reverse_lazy('home:home', kwargs={
                'id':post.id
            })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
    
    
def dump_database_view(request):
    dump_database()
    return HttpResponse('Dump started')