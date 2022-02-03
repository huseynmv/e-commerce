from django.shortcuts import render
from . models import Order, Product
from django.http import JsonResponse
import json
# Create your views here.
def product(request):
    product = Product.objects.all()
    context = {
        'product' : product
    }
    return render(request, 'product.html', context)


def cart(request):
    
    if request.user.is_authenticated:
        user = request.user.id
        order, created = Order.objects.get_or_create(user=user, status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0 }
        
        
    context = {
        'items': items,
        'order': order
    }
    return render(request, 'cart.html', context)

def single_product(request):
    return render(request, 'single-product.html')

def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action', action)
    
    print('ProductID', productID)  
    return JsonResponse('item was added', safe=False)

