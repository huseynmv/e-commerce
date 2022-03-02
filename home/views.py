from unicodedata import category
from django.shortcuts import render
from shop.models import *
from blog.models import *
# Create your views here.
def index(request):
    product = Product.objects.filter(price__range=(0, 101)).order_by("-created_at")[:2]
    blog = Blog.objects.all()[:4]
    print(blog)
    context = {
        'product':product,
        'blog':blog
    }
    return render(request, 'index.html',context)

# def base(request):
#     category = ProductCategory.objects.all()
#     context={
#         'category':category,
#     }
#     print(category)
#     return render(request, 'base.html',  context)