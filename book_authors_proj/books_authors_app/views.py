from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "lista_libro": Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    title=request.POST['title']
    description=request.POST['description']
    Book.objects.create(title=title, description=description)

    return redirect('/')

def authors(request):
    context = {
        "lista_autores": Publisher.objects.all()
    }
    return render(request, 'authors.html', context)

def add_new_author(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    notes=request.POST['notes']
    Publisher.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def add_author(request):
    book_id=request.POST['book_id']
    author_id=int(request.POST['author_id'])
    book_new_author=Publisher.objects.get(id=author_id)
    book_new_author.books.add(Book.objects.get(id=book_id))
    book_new_author.save()
    return redirect(f'books/{book_id}/')

def view_book(request, libro_id):
    book_id= libro_id
    book_authors= Publisher.objects.filter(books__id=book_id)
    context={
        "book":Book.objects.get(id=book_id),
        "publishers": Publisher.objects.all(),
        "book_authors": book_authors
    }
    return render(request, 'view_book.html', context)

def view_author(request, author_id):
    author_id= author_id
    authors_book= Book.objects.filter(publishers__id=author_id)
    context={
        "author":Publisher.objects.get(id=author_id),
        "books": Book.objects.all(),
        "authors_book": authors_book
    }
    return render(request, 'view_author.html', context)

def add_book_to_author(request):
    author_id=request.POST['author_id']
    book_id=int(request.POST['book_id'])
    author_new_book=Publisher.objects.get(id=author_id)
    author_new_book.books.add(Book.objects.get(id=book_id))
    author_new_book.save()
    return redirect(f'authors/{author_id}/')