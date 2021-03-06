from unicodedata import category
from django.shortcuts import render
from shop.models import Product
from blog.models import Blog
from .models import HomeSlider, HomeSecondarySlider
# Create your views here.
def index(request):
    product = Product.objects.all().order_by("-created_at")[:3]
    electronic = Product.objects.filter(category__name__in=['electronic', 'Electronic'])
    clothes = Product.objects.filter(category__name__in=['clothes','Clothes','wear','Wear'])
    technology = Product.objects.filter(category__name__in=['technology',"Technology", 'computer', 'Computer', ])
    blog = Blog.objects.all()[:4]
    slider = HomeSlider.objects.all()
    secondary_slider = HomeSecondarySlider.objects.all()
    print(blog)
    
    context = {
        'product':product,
        'blog':blog,
        'electronic': electronic,
        'clothes':clothes,
        'tech': technology,
        'slider':slider,
        'secondary_slider':secondary_slider,
        
    }
    return render(request, 'index.html',context)

# def base(request):
#     category = ProductCategory.objects.all()
#     context={
#         'category':category,
#     }
#     print(category)
#     return render(request, 'base.html',  context)