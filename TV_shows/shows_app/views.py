from django.shortcuts import render
from .models import *

# Create your views here.

def shows(request):

    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def add_show(request):
    return render(request, 'add_show.html')