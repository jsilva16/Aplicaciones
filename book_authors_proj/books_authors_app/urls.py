from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.index),
    path('books', views.index),
    path('add_book', views.add_book, name='add_book'),
    path('authors', views.authors, name='authors'),
    path('add_author', views.add_author, name='add_author'),
    path('add_book_to_author', views.add_book_to_author, name='add_book_to_author'),
    path('add_new_author', views.add_new_author, name='add_new_author'),
    path('books/<int:libro_id>/', views.view_book, name='libro_id'),
    path('authors/<int:author_id>/', views.view_author, name='author_id'),

    
]
