from django import forms
from .models import Sale, SaleItem

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'date', 'total_amount', 'payment_method', 'notes']

class SaleItemFormSet(forms.models.inlineformset_factory(Sale, SaleItem, fields=['product', 'quantity', 'unit_price'], extra=1)):
    pass 