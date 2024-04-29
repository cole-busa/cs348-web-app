from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Member, Loan
from .forms import BookModelForm,  MemberModelForm, LoanModelForm

def get_all(request):
    books = Book.objects.all()
    members = Member.objects.all()
    loans = Loan.objects.all()
    context = {'books': books, 'members': members, 'loans': loans}
    return render(request, 'library/get_all.html', context)

def create_book(request):
    if request.method == "POST":
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_all')
    else:
        form = BookModelForm()
    return render(request, "library/create_book.html", {"form" : form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('get_all')
    else:
        form = BookModelForm(instance=book)
    return render(request, 'library/edit_book.html', context={'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('get_all')
    return render(request, 'library/delete_book.html', context={'book': book})

def create_member(request):
    if request.method == "POST":
        form = MemberModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_all')
    else:
        form = MemberModelForm()
    return render(request, "library/create_member.html", {"form" : form})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberModelForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('get_all')
    else:
        form = MemberModelForm(instance=member)
    return render(request, 'library/edit_member.html', context={'form': form})

def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('get_all')
    return render(request, 'library/delete_member.html', context={'member': member})

def create_loan(request):
    if request.method == "POST":
        form = LoanModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_all')
    else:
        form = LoanModelForm()
    return render(request, "library/create_loan.html", {"form" : form})

def edit_loan(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == 'POST':
        form = LoanModelForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('get_all')
    else:
        form = LoanModelForm(instance=loan)
    return render(request, 'library/edit_loan.html', context={'form': form})

def delete_loan(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == 'POST':
        loan.delete()
        return redirect('get_all')
    return render(request, 'library/delete_loan.html', context={'loan': loan})

def generate_report(request):
    if request.method == 'GET':
        genres = Book.objects.values_list('genre', flat=True).distinct()
        authors = Book.objects.values_list('author', flat=True).distinct()

        selected_genres = request.GET.getlist('genre')
        selected_authors = request.GET.getlist('author')

        filtered_books = Book.objects.all()
        if selected_genres and selected_authors:
            filtered_books = Book.objects.filter(genre__in=selected_genres, author__in=selected_authors)
        elif selected_genres:
            filtered_books = Book.objects.filter(genre__in=selected_genres)
        elif selected_authors:
            filtered_books = Book.objects.filter(author__in=selected_authors)
        return render(request, 'library/report.html', {'books': filtered_books, 'genres': genres, 'authors': authors})
    return render(request, 'library/report.html', {'books': None, 'genres': None, 'authors': None})