from django.shortcuts import render
from . models import Order, OrderItem, Product
from django.http import JsonResponse
from django.views.generic import DetailView
import json
# Create your views here.
def product(request):
        if request.user.is_authenticated:
            user = request.user
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
        user = request.user
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

class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product.html' 
    context_object_name = 'product'

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
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
        'cartItems':cartItems
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
    
    if orderItem.quantity <= 0 or action == 'removeAll':
        orderItem.delete()
        
     
    return JsonResponse('item was added', safe=False)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_item = Product.objects.filter(name__icontains = searched)
        x = list(Product.objects.values_list('name', flat=True))
        print(x)
        context = {
            'search_item':search_item,
            'searched':searched,
        }
        return render(request, 'search.html',context)