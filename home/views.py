from unicodedata import category
from django.shortcuts import render
from shop.models import Product
from blog.models import Blog
# Create your views here.
def index(request):
    product = Product.objects.filter(price__range=(0, 101)).order_by("-created_at")[:2]
    electronic = Product.objects.filter(category__name__in=['electronic', 'Electronic'])
    clothes = Product.objects.filter(category__name__in=['clothes', 'wear'])
    technology = Product.objects.filter(category__name__in=['technology', 'computer'])
    print(electronic)
    blog = Blog.objects.all()[:4]
    print(blog)
    
    context = {
        'product':product,
        'blog':blog,
        'electronic': electronic,
        'clothes':clothes,
        'tech': technology,
        
    }
    return render(request, 'index.html',context)

# def base(request):
#     category = ProductCategory.objects.all()
#     context={
#         'category':category,
#     }
#     print(category)
#     return render(request, 'base.html',  context)