from unicodedata import category
from django.shortcuts import render
from shop.models import *
# Create your views here.
def index(request):
    
    return render(request, 'index.html',)

# def base(request):
#     category = ProductCategory.objects.all()
#     context={
#         'category':category,
#     }
#     print(category)
#     return render(request, 'base.html',  context)