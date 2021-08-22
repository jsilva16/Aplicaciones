from django.shortcuts import render
from django.utils.crypto import get_random_string


# Create your views here.
def random_word():
    word = get_random_string(length=14)
    return word
attempt = random_word()

def index(request):
    counter = request.session.get('counter', 1)
    request.session['counter'] = counter + 1
    context = {
        "rndStr" : get_random_string(length=14),
        "counter" : counter,
        "attempt" : attempt,
    }
    return render(request, 'index.html', context)

def reset(request):
    del request.session['counter']
    counter = request.session.get('counter', 1)
    request.session['counter'] = counter + 1
    context = {
        "rndStr" : get_random_string(length=14),
        "counter" : counter,
        "attempt" : attempt,
    }
    return render(request, 'index.html', context)
