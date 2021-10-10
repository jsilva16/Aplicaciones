from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def shows(request):

    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def add_show(request):
    return render(request, 'add_show.html')

def add_new_show(request):
    show_title = request.POST['show_title']
    release_date=request.POST['rel_date']
    description = request.POST['show_desc']
    new_network = request.POST['network']
    networks=Networks.objects.all()
    network_exist=False
    if len(networks)==0:
        Networks.objects.create(name=new_network)
        network_exist=True
    for network in networks:
        if  new_network == network.name:
            network_exist=True
            break
    if not network_exist:
        Networks.objects.create(name=new_network)

    curr_network=Networks.objects.get(name=new_network)
    Show.objects.create(title=show_title, release_date=release_date, description=description, network=curr_network)
    new_show=Show.objects.get(title=show_title)
    return redirect(f"/shows/{new_show.id}")

def edit_show(request, show_id):
    context={
        "update_show": Show.objects.get(id= show_id)
    }
    return render(request, 'edit_show.html', context)

def delete_show(request, show_id):
    del_show=Show.objects.get(id= show_id)
    del_show.delete()
    return redirect('/')

def view_show(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, 'view_show.html', context)

def update_show(request, show_id):
    updating_show= Show.objects.get(id= show_id)
    if len(request.POST['update_show_title'])!= 0:
        updating_show.title=request.POST['update_show_title']
    if len(request.POST['update_network'])!= 0:
        update_network=request.POST['update_network']
        network_exist=False
        networks=Networks.objects.all()
        for network in networks:
            if  update_network == network.name:
                network_exist=True
                break
        if not network_exist:
            Networks.objects.create(name=update_network)
        updated_network=Networks.objects.get(name=update_network)
        updating_show.network=updated_network
    if len(request.POST['update_rel_date'])!= 0:
        updating_show.release_date=request.POST['update_rel_date']
    if len(request.POST['update_show_desc'])!= 0:
        updating_show.description=request.POST['update_show_desc']
    updating_show.save()
    return redirect(f"/shows/{request.POST['update_show_id']}")