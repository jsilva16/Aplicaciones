from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.index),
    path('time_display', views.index),
]
