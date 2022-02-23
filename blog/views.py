
from gc import get_objects
from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Blog, Comment
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
            form.save()
            return redirect(reverse_lazy('home:home'))
    
    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.all()
        comment_count = Comment.objects.all().count()
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'comment': post_comments,
            'count': comment_count
        })
        return context
    
    
def dump_database_view(request):
    dump_database()
    return HttpResponse('Dump started')

def blog_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_item = Blog.objects.filter(name__icontains = searched)
        context = {
            'search_item':search_item,
            'searched':searched,
        }
        return render(request, 'blog-search.html',context)