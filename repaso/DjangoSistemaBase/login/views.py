from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
import bcrypt

from .models import *

# Create your views here.
def login(request):
    return render(request, 'registro.html')
def registrar(request):
    return render(request, 'registro.html')


def inicio2(request):
    email2=request.POST['email2']
    perro=request.POST['perro']
    password=request.POST['password']

    #creacion en base de datos del poke
    poke = Poke.objects.create(
        email=request.POST['email2'],
        perro=request.POST['perro'],
        password=request.POST['password']
    )

    context={
        'gato' : email2,
        'elefante':perro,
        'avion':password,
        'lista_pokes': Poke.objects.all()
    }
    return render(request, 'prueba.html', context)


def inicio(request):
    usuario = User.objects.filter(email=request.POST['email'])
    errores = User.objects.validar_login(request.POST, usuario)

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = usuario[0].id
        return redirect('home/')

def registro(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registrar')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        decode_hash_pw = password.decode('utf-8')
        #crear usuario
        if request.POST['rol'] == '1':
            user = User.objects.create(
                nombre=request.POST['nombre'],
                alias=request.POST['alias'],
                cumple=request.POST['cumple'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=1,
            )
        else:
            user = User.objects.create(
                nombre=request.POST['nombre'],
                alias=request.POST['alias'],
                cumple=request.POST['cumple'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=2,
            )
        request.session['user_id'] = user.id
    return redirect('home/')

def logout(request):
    request.session.flush()
    return redirect('/')

def pet_reg(request):
    name=request.POST['name']
    age=request.POST['age']
    sex=request.POST['sex']
    race=request.POST['race']

    pets= Mascotas.objects.create(
        name=request.POST['name'],
        age=request.POST['age'],
        sex=request.POST['sex'],
        race=request.POST['race']
    )

    context={
        'name': name,
        'age': age,
        'sex': sex,
        'race': race,
        'lista_pets': Mascotas.objects.all()
    }
    return render(request, 'pets.html', context)

def delete(request):
    Mascotas.objects.get(id=request.POST['id']).delete()
    return render(request, 'pets.html')

def addpoke(request):
    recept_id=request.POST['receptor_id']
    emissor_id=request.session['user_id']
    toque_receptor=User.objects.get(id='recept_id')
    toque_receptor.historico +=1 #suma un toque al usuario receptor
    #poke= Poke.objects.create(emisor=emissor_id, receptor=recept_id)
    return render(request, 'home.html')

