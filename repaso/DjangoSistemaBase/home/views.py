from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from login.models import *


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['user_id'])
    poke_users= Poke.objects.filter(receptor =reg_user, ).count()
    poke_count = Poke.objects.values('emisor_id').count()
    poke_user = Poke.objects.filter(receptor = reg_user).values('emisor').annotate(total=Count('emisor')).order_by('total')
    
    pokearr=[]
    for user in poke_user:
        print ("******",user["emisor"])
        pokearr.append({
            "emisor":User.objects.filter(id=user["emisor"]),
            "total":user["total"]
        })
    
    context = {
        "active_user": reg_user,
        "lista_users": User.objects.all(),
        "poke_users" : poke_users,
        "poke_user" : poke_user,
        "pokearr" :pokearr
    }


    return render(request, 'home.html', context)

def addpoke(request):
    #recept_id=request.POST['receptor_id']
    toque_receptor=User.objects.get(id=request.POST['receptor_id'])
    toque_receptor.historico +=1 #suma un toque al usuario receptor
    toque_receptor.save()
    emissor_id= User.objects.get(id=request.session['user_id'])
    poke= Poke.objects.create(emisor=emissor_id, receptor=toque_receptor)
    
    return redirect('/home')
