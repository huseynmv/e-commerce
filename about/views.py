from django.shortcuts import render
from .models import Leaders

# Create your views here.
def about(request):
    leader = Leaders.objects.all()
    context = {
        'leader': leader,
        }
    return render(request, 'about-us.html', context)