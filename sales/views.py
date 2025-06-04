from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
# from weasyprint import HTML
from django.template.loader import render_to_string
from .models import Sale, SaleItem
from .forms import SaleForm, SaleItemFormSet
from inventory.models import Product

@login_required
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})

@login_required
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        formset = SaleItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            sale = form.save(commit=False)
            sale.invoice_number = f"INV-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            sale.save()
            formset.instance = sale
            formset.save()
            messages.success(request, 'Sale created successfully!')
            return redirect('sales:sale_detail', pk=sale.pk)
    else:
        form = SaleForm()
        formset = SaleItemFormSet()
    return render(request, 'sales/sale_form.html', {
        'form': form,
        'formset': formset,
        'title': 'New Sale'
    })

@login_required
def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/sale_detail.html', {'sale': sale})

@login_required
def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        formset = SaleItemFormSet(request.POST, instance=sale)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Sale updated successfully!')
            return redirect('sales:sale_detail', pk=pk)
    else:
        form = SaleForm(instance=sale)
        formset = SaleItemFormSet(instance=sale)
    return render(request, 'sales/sale_form.html', {
        'form': form,
        'formset': formset,
        'title': 'Edit Sale'
    })

@login_required
def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale.delete()
        messages.success(request, 'Sale deleted successfully!')
        return redirect('sales:sale_list')
    return render(request, 'sales/sale_confirm_delete.html', {'sale': sale})

@login_required
def generate_invoice(request, pk):
    # sale = get_object_or_404(Sale, pk=pk)
    # html_string = render_to_string('sales/invoice.html', {'sale': sale})
    # html = HTML(string=html_string)
    # pdf = html.write_pdf()
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="invoice_{sale.invoice_number}.pdf"'
    # return response
    pass

# Create your views here.
