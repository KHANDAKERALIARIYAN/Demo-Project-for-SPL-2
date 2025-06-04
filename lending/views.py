from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LendingRecord
from .forms import LendingRecordForm
from django.utils import timezone

# Create your views here.

@login_required
def lending_list(request):
    records = LendingRecord.objects.all()
    return render(request, 'lending/lending_list.html', {'records': records})

@login_required
def lending_create(request):
    if request.method == 'POST':
        form = LendingRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lending record created successfully!')
            return redirect('lending:lending_list')
    else:
        form = LendingRecordForm()
    return render(request, 'lending/lending_form.html', {
        'form': form,
        'title': 'New Lending Record'
    })

@login_required
def lending_detail(request, pk):
    record = get_object_or_404(LendingRecord, pk=pk)
    return render(request, 'lending/lending_detail.html', {'record': record})

@login_required
def lending_update(request, pk):
    record = get_object_or_404(LendingRecord, pk=pk)
    if request.method == 'POST':
        form = LendingRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lending record updated successfully!')
            return redirect('lending:lending_detail', pk=pk)
    else:
        form = LendingRecordForm(instance=record)
    return render(request, 'lending/lending_form.html', {
        'form': form,
        'title': 'Edit Lending Record'
    })

@login_required
def lending_delete(request, pk):
    record = get_object_or_404(LendingRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, 'Lending record deleted successfully!')
        return redirect('lending:lending_list')
    return render(request, 'lending/lending_confirm_delete.html', {'record': record})

@login_required
def lending_return(request, pk):
    record = get_object_or_404(LendingRecord, pk=pk)
    if request.method == 'POST':
        record.return_date = timezone.now()
        record.save()
        messages.success(request, 'Item returned successfully!')
        return redirect('lending:lending_detail', pk=pk)
    return render(request, 'lending/lending_return.html', {'record': record})
