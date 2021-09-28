from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def login(request):
    user = User.objects.filter(username=request.POST['login_username'])
    #errores = User.objects.validate_login(request.POST, user)
    request.session['user_id'] = user[0].id
    return redirect('travels')
    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = user[0].id
        return redirect('travels')


def home(request):
    return render(request, 'welcome.html')



def register(request):
    #metodo de validacion desde los models
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    #en caso de no encontrar errores prosigue a la creacion de usuario y encriptación de password
    else:
        #metodo de encriptacion desde los models
        password = User.objects.encriptar(request.POST['password'])
        decoded_pass = password.decode('utf-8')
        
        #creacion de usuario
        user = User.objects.create(
            name=request.POST['name'],
            username=request.POST['username'],
            password=decoded_pass,
        )
        msg="Usuario creado exitosamente!"
        messages.success(request, msg)
    return redirect('/')



def logout(request):
    request.session.flush()
    return redirect('/')

def add_trip(request):

    return render(request, 'add_trip.html')

def view_trip(trip_id, request):
    
    return render(request, 'add_trip.html')

def travels(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    context = {
        "active_user": reg_user,
        "trips":Trip.objects.filter(users=reg_user),
        "all_trips":Trip.objects.all()
    }

    return render(request, 'travels.html', context)

def add_new_trip(request):
    user= User.objects.get(id=request.session['user_id'])
    print("**************",user,"***********")
    destination= request.POST['destination']
    description= request.POST['description']
    start_date= request.POST['start_date']
    end_date= request.POST['end_date']
    new_trip=Trip.objects.create(destination=destination, description=description, start_date= start_date, end_date=end_date, users=user)
    return render(request, 'travels.html')
