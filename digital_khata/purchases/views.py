from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bill, BillItem
from .forms import BillForm, BillItemForm
from accounts.models import Supplier
from inventory.models import Product
from django.forms import inlineformset_factory
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import BillSerializer
from accounts.models import BusinessProfile


# API Views
class BillListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Set the user and business from the request context
        request = self.request
        if request and hasattr(request, 'user'):
            # Set business from user's business profile
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                serializer.save(user=request.user, business=business_profile)
            except BusinessProfile.DoesNotExist:
                serializer.save(user=request.user)

class BillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)

@login_required
def bill_list(request):
    bills = Bill.objects.filter(user=request.user)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        bills = bills.filter(
            Q(bill_number__icontains=search_query) | 
            Q(supplier__name__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        bills = bills.filter(status=status_filter)
    
    return render(request, 'purchases/bill_list.html', {
        'bills': bills,
        'search_query': search_query
    })

@login_required
def bill_create(request):
    BillItemFormSet = inlineformset_factory(
        Bill, BillItem, form=BillItemForm, extra=1
    )
    
    if request.method == 'POST':
        form = BillForm(request.POST)
        formset = BillItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()
            
            formset.instance = bill
            formset.save()
            
            # Update product quantities
            update_product_quantities(bill, is_purchase=True)
            
            messages.success(request, 'Bill created successfully!')
            return redirect('purchases:bill_list')
    else:
        form = BillForm()
        formset = BillItemFormSet()
    
    return render(request, 'purchases/bill_form.html', {
        'form': form,
        'formset': formset
    })

@login_required
def bill_update(request, pk):
    bill = get_object_or_404(Bill, pk=pk, user=request.user)
    BillItemFormSet = inlineformset_factory(
        Bill, BillItem, form=BillItemForm, extra=1
    )
    
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        formset = BillItemFormSet(request.POST, instance=bill)
        
        if form.is_valid() and formset.is_valid():
            # Store old quantities before updating
            old_items = list(bill.items.all())
            
            form.save()
            formset.save()
            
            # Update product quantities
            revert_product_quantities(old_items)
            update_product_quantities(bill, is_purchase=True)
            
            messages.success(request, 'Bill updated successfully!')
            return redirect('purchases:bill_list')
    else:
        form = BillForm(instance=bill)
        formset = BillItemFormSet(instance=bill)
    
    return render(request, 'purchases/bill_form.html', {
        'form': form,
        'formset': formset
    })

@login_required
def bill_delete(request, pk):
    bill = get_object_or_404(Bill, pk=pk, user=request.user)
    if request.method == 'POST':
        # Revert product quantities before deleting
        revert_product_quantities(bill.items.all())
        bill.delete()
        messages.success(request, 'Bill deleted successfully!')
        return redirect('purchases:bill_list')
    return render(request, 'purchases/bill_confirm_delete.html', {'bill': bill})

def update_product_quantities(bill, is_purchase=True):
    """Update product quantities when bill is created/updated"""
    for item in bill.items.all():
        product = item.product
        if is_purchase:
            product.quantity += item.quantity
        else:
            product.quantity -= item.quantity
        product.save()

def revert_product_quantities(items):
    """Revert product quantities when bill is deleted/updated"""
    for item in items:
        product = item.product
        product.quantity -= item.quantity
        product.save()