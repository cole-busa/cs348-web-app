from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/<int:pk>/edit/', views.edit_member, name='edit_member'),
    path('members/<int:pk>/delete/', views.delete_member, name='delete_member'),
    path('loans/create/', views.create_loan, name='create_loan'),
    path('loans/<int:pk>/edit/', views.edit_loan, name='edit_loan'),
    path('loans/<int:pk>/delete/', views.delete_loan, name='delete_loan'),
    path('generate-report/', views.generate_report, name='generate_report')
]