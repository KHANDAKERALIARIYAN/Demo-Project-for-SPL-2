from django import forms
from .models import LendingRecord

class LendingRecordForm(forms.ModelForm):
    class Meta:
        model = LendingRecord
        fields = ['customer', 'product', 'quantity', 'due_date', 'notes']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        } 