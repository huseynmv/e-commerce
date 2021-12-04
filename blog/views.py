from django.shortcuts import render

# Create your views here.

def blog_details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')
