from django.db import models
from django.core.validators import RegexValidator

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, validators=[RegexValidator(r'^\d{1,10}$')], unique=True)
    genre = models.CharField(max_length=100)

class Member(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.EmailField(unique=True)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)