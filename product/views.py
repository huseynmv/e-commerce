from django.shortcuts import render

# Create your views here.
def checkout(request):
    return render(request, 'checkout.html')

def order_tracking(request):
    return render(request, 'order-tracking.html')

def shop(request):
    return render(request, 'shop.html')

def single_product(request):
    return render(request, 'single-product.html')
