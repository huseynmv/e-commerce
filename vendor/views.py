from django.shortcuts import render

# Create your views here.
def vendor(request):
    return render(request, 'vendor.html')

def single_vendor(request):
    return render(request, 'vendor-single.html')