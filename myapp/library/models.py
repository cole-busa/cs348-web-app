from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.indexes import HashIndex

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, validators=[RegexValidator(r'^\d{13}$')], unique=True)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = (HashIndex(fields=('isbn',)),)

class Member(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = (HashIndex(fields=('contact_info',)),)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)