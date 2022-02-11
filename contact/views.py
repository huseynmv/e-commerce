from django.shortcuts import redirect, render
from . forms import ContactForm
from . models import Contact
# Create your views here.
def contact(request):
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        'form':form
    }
    
    return render(request, 'contact-us.html', context)