from django.shortcuts import render
from time import localtime, strftime
import datetime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M", localtime()),
        "timealt": datetime.datetime.now()
    }
    return render(request, 'index.html', context)

# Create your views here.
