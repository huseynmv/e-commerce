from django.shortcuts import render
# Create your views here.
def error(request):
    return render(request, 'error-404.html')

def vendor(request):
    return render(request, 'become-a-vendor.html')

def compare(request):
    return render(request, 'compare.html')

def faq(request):
    return render(request, 'faq.html')

def order(request):
    return render(request, 'order.html')

def order_view(request):
    return render(request, 'order-view.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def checkout(request):
    return render(request, 'checkout.html')