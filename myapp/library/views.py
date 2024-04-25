from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookModelForm

def get_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library/get_books.html', context)

def create_book(request):
    if request.method == "POST":
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_books')
    else:
        form = BookModelForm()
    return render(request, "library/create_book.html", {"form" : form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('get_books')
    else:
        form = BookModelForm(instance=book)
    return render(request, 'library/edit_book.html', context={'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('get_books')
    return render(request, 'library/delete_book.html', context={'book': book})