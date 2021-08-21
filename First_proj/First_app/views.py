from django.db.models.fields import EmailField
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse


def json(request):
    return JsonResponse({"key": "value"})

#from .models import Cliente
def index(request):
    redirect("/")
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")
    #return render(request,"index.html")
# Create your views here.
def method1(request):    
    pass

def inicio(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):     
    return HttpResponse("placeholder para crear un nuevo blog")

def create(request):
    return redirect("/")

def number(request, my_val):
    return HttpResponse(f"placeholder para mostrar el blog numero {my_val}")

def edit(request, my_val):
    return HttpResponse(f"placeholder para editar el blog numero {my_val}")

def delete(request, my_val):
    return redirect("/")
