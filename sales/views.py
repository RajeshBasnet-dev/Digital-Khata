from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from datetime import date
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm

@login_required
def invoice_list(request):
    """Display list of invoices"""
    invoices = Invoice.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'sales/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_create(request):
    """Create a new invoice"""
    if request.method == 'POST':
        # Handle form submission
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user
            invoice.save()
            messages.success(request, 'Invoice created successfully!')
            return redirect('sales:invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm()
    
    context = {
        'form': form,
        'today': date.today().strftime('%Y-%m-%d')
    }
    return render(request, 'invoice_create.html', context)

@login_required
def invoice_detail(request, invoice_id):
    """Display invoice details"""
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    return render(request, 'sales/invoice_detail.html', {'invoice': invoice})

@login_required
def invoice_edit(request, invoice_id):
    """Edit an existing invoice"""
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice updated successfully!')
            return redirect('sales:invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
    
    return render(request, 'sales/invoice_form.html', {
        'form': form,
        'invoice': invoice,
        'title': 'Edit Invoice'
    })

@login_required
def invoice_delete(request, invoice_id):
    """Delete an invoice"""
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    
    if request.method == 'POST':
        invoice.delete()
        messages.success(request, 'Invoice deleted successfully!')
        return redirect('sales:invoice_list')
    
    return render(request, 'sales/invoice_confirm_delete.html', {'invoice': invoice})

@login_required
def invoice_print(request, invoice_id):
    """Print an invoice"""
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    return render(request, 'sales/invoice_print.html', {'invoice': invoice})