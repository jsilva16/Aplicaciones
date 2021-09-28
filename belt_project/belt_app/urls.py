from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_trip', views.add_trip, name='add_trip'),
    path('add_new_trip', views.add_new_trip, name='add_new_trip'),
    path('travels', views.travels, name='travels'),
    path('travels/destination/<int:trip_id>', views.view_trip, name='view_trip'),

    
    #path('users/<int:user_id>', views.view_user, name='view_user'),
    #path('cambiar_pass', views.cambiar_pass, name='cambiar_pass'),
]