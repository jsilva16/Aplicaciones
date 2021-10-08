from django.urls import path
from . import views

urlpatterns = [
	path('', views.shows, name="home"),
	path('shows', views.shows, name="shows"),
	path('shows/new', views.add_show, name="shows"),
	

]
