from django.shortcuts import render
from . models import Order, OrderItem, Product
from django.http import JsonResponse
import json
# Create your views here.
def product(request):
        if request.user.is_authenticated:
            user = request.user.id
            order, created = Order.objects.get_or_create(user=user, status=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0,'get_cart_items': 0 }
            cartItems = order['get_cart_items']
        product = Product.objects.all()
        context = {
            'product' : product,
            'cartItems': cartItems
        }
        return render(request, 'product.html', context)


def cart(request):
    
    if request.user.is_authenticated:
        user = request.user.id
        order, created = Order.objects.get_or_create(user=user, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0 }
        cartItems = order['get_cart_items']
        
        
        
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'cart.html', context)

def single_product(request):
    return render(request, 'single-product.html')

def checkout(request):
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
    return render(request, 'checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action', action)
    print('ProductID', productID) 
    
    user = request.user.id
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(user=user, status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete() 
        
     
    return JsonResponse('item was added', safe=False)

