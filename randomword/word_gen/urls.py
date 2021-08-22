from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.index),
    path('word_gen', views.index),
    path('reset', views.reset),
]
