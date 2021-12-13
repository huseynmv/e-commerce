from django.core.mail.message import sanitize_address
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import RegistrationForm
from django.contrib import messages
from account.tasks import send_confirmation_mail
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from account.tools.tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout


User = get_user_model()
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
            user.is_active = False
            return redirect(reverse_lazy('home:home'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:home'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('account:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('account:register'))