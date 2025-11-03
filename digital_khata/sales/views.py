from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from accounts.models import Customer
from inventory.models import Product
from django.forms import inlineformset_factory
from django.db.models import Q

@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=search_query) | 
            Q(customer__name__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        invoices = invoices.filter(status=status_filter)
    
    return render(request, 'sales/invoice_list.html', {
        'invoices': invoices,
        'search_query': search_query
    })

@login_required
def invoice_create(request):
    InvoiceItemFormSet = inlineformset_factory(
        Invoice, InvoiceItem, form=InvoiceItemForm, extra=1
    )
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user
            invoice.save()
            
            formset.instance = invoice
            formset.save()
            
            # Update product quantities
            update_product_quantities(invoice, is_sale=True)
            
            messages.success(request, 'Invoice created successfully!')
            return redirect('sales:invoice_list')
    else:
        form = InvoiceForm()
        formset = InvoiceItemFormSet()
    
    return render(request, 'sales/invoice_form.html', {
        'form': form,
        'formset': formset
    })

@login_required
def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk, user=request.user)
    InvoiceItemFormSet = inlineformset_factory(
        Invoice, InvoiceItem, form=InvoiceItemForm, extra=1
    )
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        
        if form.is_valid() and formset.is_valid():
            # Store old quantities before updating
            old_items = list(invoice.items.all())
            
            form.save()
            formset.save()
            
            # Update product quantities
            revert_product_quantities(old_items)
            update_product_quantities(invoice, is_sale=True)
            
            messages.success(request, 'Invoice updated successfully!')
            return redirect('sales:invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
        formset = InvoiceItemFormSet(instance=invoice)
    
    return render(request, 'sales/invoice_form.html', {
        'form': form,
        'formset': formset
    })

@login_required
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk, user=request.user)
    if request.method == 'POST':
        # Revert product quantities before deleting
        revert_product_quantities(invoice.items.all())
        invoice.delete()
        messages.success(request, 'Invoice deleted successfully!')
        return redirect('sales:invoice_list')
    return render(request, 'sales/invoice_confirm_delete.html', {'invoice': invoice})

def update_product_quantities(invoice, is_sale=True):
    """Update product quantities when invoice is created/updated"""
    for item in invoice.items.all():
        product = item.product
        if is_sale:
            product.quantity -= item.quantity
        else:
            product.quantity += item.quantity
        product.save()

def revert_product_quantities(items):
    """Revert product quantities when invoice is deleted/updated"""
    for item in items:
        product = item.product
        product.quantity += item.quantity
        product.save()