from django import forms

from borrowing.models import Borrowing

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ("emprunteur", "date")