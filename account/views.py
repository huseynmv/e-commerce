from django.shortcuts import redirect, render
from . forms import  RegistrationForm
from django.urls import reverse_lazy
# Create your views here.
def login(request):
    return render(request, 'login.html')

def my_account(request):
    return render(request, 'my-account.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data =request.POST, files = request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password = form .cleaned_data.get('password1')
            user.save()
            return redirect(reverse_lazy('home:home'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)