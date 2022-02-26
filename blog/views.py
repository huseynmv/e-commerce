
from gc import get_objects
from turtle import pos
from taggit.models import Tag 
from modulefinder import replacePackageMap
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.http import HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, redirect, render
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
    ontext_object_name = 'blog_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blog.objects.all()
        blog_category = BlogCategory.objects.all()
        context = {
            'blog_list':blog,
            'category': blog_category
        }   
        return context  



class TagIndexView(ListView):
    model = Blog
    template_name = 'tags.html'
    paginate_by = 3
    context_object_name = 'blog_list'
    
    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
    #kwargs.get('slug')

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
            return redirect(reverse_lazy('blog:blog-details', kwargs={
                'slug':post.slug
            }))
            
    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.all().filter(post=self.object.id)
        comment_count = Comment.objects.all().filter(post=self.object.id).count()
        recent_blogs = Blog.objects.order_by("-date")[:3]
        # blog = Blog.objects.tags.all().filter(id=self.object.id)
        tags = list(Blog.objects.filter(id=self.object.id).values_list('tags__name', flat=True))
        print(tags)
        context = super().get_context_data(**kwargs)
        related_blog = Blog.objects.filter(category=self.object.category).exclude(name=self.object.name)
        
        context.update({
            'form': self.form,
            'comment': post_comments,
            'count': comment_count,
            'recent_blogs':recent_blogs,
            'related_blog':related_blog,
            'tags':tags
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
    
    
def blog_filter(request, slug):
    blog = Blog.objects.filter(category__slug=slug)
    blogCategory = BlogCategory.objects.all()
    context = {
        'blog':blog,
        'blogCategory':blogCategory,
    }
    return render(request, 'blog-filter.html', context)