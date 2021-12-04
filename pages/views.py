from django.shortcuts import render

# Create your views here.

def customer_service(request):
    return render(request, 'customer-service.html')

def faq(request):
    return render(request, 'faq.html')

def privacy(request):
    return render(request, 'privacy-policy.html')

def product_on_sale(request):
    return render(request, 'products-on-sale.html')

def policy(request):
    return render(request, 'return-policy.html')

def conditions(request):
    return render(request, 'terms-conditions.html')