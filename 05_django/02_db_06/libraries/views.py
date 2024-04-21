from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm


# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = AuthorForm()
    context = {
        'form': form,
    }
    return render(request, 'libraries/create_author.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'libraries/books.html', context)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
    else:
        form = BookForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'libraries/create_book.html', context)

def author_books(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    context = {
        'author': author,
    }
    return render(request, 'libraries/author_books.html', context)

def subscribe(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    if request.user in author.subscribed_users.all():
        author.subscribed_users.remove(request.user)
    else:
        author.subscribed_users.add(request.user)
    return redirect('libraries:author_books', author_pk)