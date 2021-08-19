from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.index),
    #path('inicio', views.inicio),
    #path('agregar', views.agregar),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:my_val>', views.number),
    path('blogs/<int:my_val>/edit', views.edit),
    path('blogs/<int:my_val>/delete', views.delete),

]
