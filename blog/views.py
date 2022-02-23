
from gc import get_objects
from modulefinder import replacePackageMap
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Blog, BlogCategory, Comment
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
        recent_blogs = Blog.objects.order_by("-date")[:3]
        context = super().get_context_data(**kwargs)
        # current_blog = Blog.objects.filter(id=Blog.objects.values_list('id', flat=True))
        related_blog = Blog.objects.filter(category=self.object.category).exclude(name=self.object.name)
        print(related_blog)
        context.update({
            'form': self.form,
            'comment': post_comments,
            'count': comment_count,
            'recent_blogs':recent_blogs,
            'related_blog':related_blog
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