from django.urls import path
from . import views


app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_author/', views.create_author, name='create_author'),
    path('books/', views.books, name='books'),
    path('books/create/', views.create_book, name='create_book'),
    path('author_books/<int:author_pk>/', views.author_books, name='author_books'),
    path('<int:author_pk>/subscribe/', views.subscribe, name='subscribe'),
]
