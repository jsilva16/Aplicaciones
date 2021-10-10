from django.urls import path
from . import views

urlpatterns = [
	path('', views.shows, name="home"),
	path('shows', views.shows, name="shows"),
	path('shows/new', views.add_show, name="shows"),
	path('shows/add_new_show', views.add_new_show, name="shows"),
	path('shows/<int:show_id>/edit', views.edit_show, name='edit_show'),
	path('shows/<int:show_id>/update_show', views.update_show, name='update_show'),
	path('shows/<int:show_id>/delete', views.delete_show, name='delete_show'),
	path('shows/<int:show_id>', views.view_show, name='view_show'),
	

]
