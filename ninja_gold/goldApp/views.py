from django.shortcuts import redirect, render
from random import randint

# Create your views here.

def index(request):
    if 'money' not in request.session:
        request.session['money'] = 0
    return render(request, 'index.html')

def process_money(request):
    if "farm" in request.POST:  #pregunta si el valor farm esta en el formulario
        r_farm=randint(10,20)   #se obtiene un valor aleatorio entre 10 y 20
        request.session['money'] += r_farm

    if "cave" in request.POST:  #pregunta si el valor farm esta en el formulario
        r_cave=randint(5,10)   #se obtiene un valor aleatorio entre 5 y 10
        request.session['money'] += r_cave

    if "house" in request.POST:  #pregunta si el valor farm esta en el formulario
        r_house=randint(2,5)   #se obtiene un valor aleatorio entre 2 y 5
        request.session['money'] += r_house

    if "casino" in request.POST:  #pregunta si el valor farm esta en el formulario
        r_casino=randint(-50,50)   #se obtiene un valor aleatorio entre -50 y 50
        request.session['money'] += r_casino
        
    return redirect('/')