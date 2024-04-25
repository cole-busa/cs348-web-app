from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books, name='get_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]