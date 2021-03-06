import colorsys
from django.shortcuts import render

from .forms import CheckoutForm
from . models import Brand, Color, Order, OrderItem, Product, ProductCategory, WishlistItem,Wishlist, Discount
from django.http import JsonResponse
from django.views.generic import DetailView
from django.template.loader import render_to_string
from django.db.models import Q
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
        categories = list(ProductCategory.objects.all().values_list('name', flat=True))
        brand = Brand.objects.all()
        color  = Color.objects.all()
        a = list(Product.objects.all().values_list('category',flat=True))
        percent = list(ProductCategory.objects.values_list('discount_percent', flat=True))
        discount_price = list(Product.objects.all().values_list('price', flat=True))
        
        print(percent)
        for j in percent:
            print(j)
            for i in discount_price:
                p = i - i * j / 100
                print(p)
        context = {
            'product' : product,
            'cartItems': cartItems,
            'categories':categories,
            'brand':brand,
            'color': color,
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


# def cart(request):
#     return render(request, 'cart.html', {'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product.html' 
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_product = Product.objects.filter(category=self.object.category).exclude(name=self.object.name)
        more_product = Product.objects.all().order_by('-id')[:3]
        
        context.update({
            'related_product':related_product,
            'more_product': more_product
        })
        return context

def checkout(request):
    if request.user.is_authenticated:
        message_send = False
        form = CheckoutForm()
        if request.method == 'POST':
            form = CheckoutForm(data=request.POST)
            if form.is_valid():
                message_send = True
                
             
                    
                form.save()
                    
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
        'cartItems':cartItems,
        'form':form,
        'message_send':message_send
    }
    return render(request, 'checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    user = request.user.id
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(user=user, status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    oitemcount = OrderItem.objects.all().count()
    print('salam')
    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
        print('added')
        
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()
    
    if orderItem.quantity <= 0 or action == 'removeAll':
        orderItem.delete()
        
        
    if oitemcount <= 1 and (action == 'removeAll' or action == 'remove'):
        order.delete()
        
     
    return JsonResponse('item was added', safe=False)

# def update_item(request):
# 	print(request.GET['image'])
# 	cart_p={}
# 	cart_p[str(request.GET['id'])]={
# 		'image':request.GET['image'],
# 		'title':request.GET['title'],
# 		'qty':request.GET['qty'],
# 		# 'price':request.GET['price'],
# 	}
# 	if 'cartdata' in request.session:
# 		if str(request.GET['id']) in request.session['cartdata']:
# 			cart_data=request.session['cartdata']
# 			cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
# 			cart_data.update(cart_data)
# 			request.session['cartdata']=cart_data
# 		else:
# 			cart_data=request.session['cartdata']
# 			cart_data.update(cart_p)
# 			request.session['cartdata']=cart_data
# 	else:
# 		request.session['cartdata']=cart_p
# 	return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})



def wishlist(request):
    datas = json.loads(request.body)
    productID = datas['p']
    action = datas['a']

    
    user = request.user
    product = Product.objects.get(id=productID)
    wishlist, created = Wishlist.objects.get_or_create(user=user, status=False)
    wishlistitem, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
    if action == 'addWishlist':
        wishlistitem.quantity = (wishlistitem.quantity + 1)

    elif action == 'removeWishlist':
        wishlistitem.quantity = 0     
    wishlistitem.save()

    if wishlistitem.quantity == 0:        
        wishlistitem.delete()

     
    return JsonResponse('item was added', safe=False)



def wishlist_view(request):
        
    if request.user.is_authenticated:
        user = request.user
        wishlist, created = Wishlist.objects.get_or_create(user=user, status=False)
        items = wishlist.wishlistitem_set.all()
        # cartItems = order.get_cart_items
        
    else:
        items = []
        # order = {'get_cart_total': 0,'get_cart_items': 0 }
        # cartItems = order['get_cart_items']
        
        
        
    context = {
        'items': items,
        # 'order': order,
        # 'cartItems': cartItems
    }
    return render(request, 'wishlist.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        
        search_item = Product.objects.filter(
        Q(name__icontains=searched) | Q(desc__icontains=searched)
    )   
        print(search_item)     
        context = {
            'search_item':search_item,
            'searched':searched,
        }
        return render(request, 'search.html',context)

    
def filter(request, slug):
    product = Product.objects.filter(category__slug=slug)
    category = ProductCategory.objects.filter(slug=slug).first()
    context = {
        'product':product,
        'category':category,
    }
    return render(request, 'filter.html', context)


# def filter_data(request):
# 	colors=list(Color.objects.all().values_list('id', flat=True))
#     # data = json.loads(request.body)
    
# 	# brands=request.GET.getlist('brand[]')
	 
# 	allProducts=Product.objects.all().order_by('-id').values_list('name',flat=True)
# 	# if len(brands)>0:
# 	# 	allProducts=allProducts.filter(brand__id__in=brands).distinct()
# 	t=render_to_string('ajax/product.html',{'data':allProducts})
 
# 	return JsonResponse({'data':t})


def filter_data(request):
    allprod=Product.objects.all()
    color = request.GET.getlist('color[]')
    # color = list(Color.objects.all().values_list('id', flat=True))
    
    brand = request.GET.getlist('brand[]')

    if len(color)>0:
      
        
        allprod=allprod.filter(color__name__in = color)
        
    if len(brand)>0:
        
        
        allprod=allprod.filter(brand__name__in = brand)
        
        
    t = render_to_string('ajax/yusif.html', {'data': allprod})
        
    return JsonResponse({'data':t})