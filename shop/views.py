from django.shortcuts import render
from . models import Product
from django.http import JsonResponse
import json
# Create your views here.
def product(request):
    product = Product.objects.all()
    context = {
        'product' : product
    }
    return render(request, 'product.html', context)

def single_product(request):
    return render(request, 'single-product.html')

def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action', action)
    
    print('ProductID', productID)  
    return JsonResponse('item was added', safe=False)

