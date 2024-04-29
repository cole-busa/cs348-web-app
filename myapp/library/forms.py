from django import forms
from .models import Book, Member, Loan

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MemberModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class LoanModelForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'