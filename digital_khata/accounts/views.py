from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, CustomerForm, SupplierForm, BusinessProfileForm
from .models import Customer, Supplier, BusinessProfile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('accounts:business_setup')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Check if user has completed business setup
            try:
                BusinessProfile.objects.get(user=user)
                return redirect('dashboard:dashboard')
            except BusinessProfile.DoesNotExist:
                return redirect('accounts:business_setup')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def business_setup(request):
    try:
        # If business profile already exists, redirect to dashboard
        business_profile = BusinessProfile.objects.get(user=request.user)
        return redirect('dashboard:dashboard')
    except BusinessProfile.DoesNotExist:
        if request.method == 'POST':
            form = BusinessProfileForm(request.POST)
            if form.is_valid():
                business_profile = form.save(commit=False)
                business_profile.user = request.user
                business_profile.owner_name = request.user.get_full_name() or request.user.username
                business_profile.save()
                messages.success(request, 'Business profile created successfully!')
                return redirect('dashboard:dashboard')
        else:
            form = BusinessProfileForm(initial={'owner_name': request.user.get_full_name() or request.user.username})
        return render(request, 'accounts/business_setup.html', {'form': form})

@login_required
def customer_list(request):
    customers = Customer.objects.filter(user=request.user)
    return render(request, 'accounts/customer_list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, 'Customer created successfully!')
            return redirect('accounts:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'accounts/customer_form.html', {'form': form})

@login_required
def customer_update(request, pk):
    customer = Customer.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully!')
            return redirect('accounts:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'accounts/customer_form.html', {'form': form})

@login_required
def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully!')
        return redirect('accounts:customer_list')
    return render(request, 'accounts/customer_confirm_delete.html', {'customer': customer})

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.filter(user=request.user)
    return render(request, 'accounts/supplier_list.html', {'suppliers': suppliers})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user
            supplier.save()
            messages.success(request, 'Supplier created successfully!')
            return redirect('accounts:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'accounts/supplier_form.html', {'form': form})

@login_required
def supplier_update(request, pk):
    supplier = Supplier.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier updated successfully!')
            return redirect('accounts:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'accounts/supplier_form.html', {'form': form})

@login_required
def supplier_delete(request, pk):
    supplier = Supplier.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Supplier deleted successfully!')
        return redirect('accounts:supplier_list')
    return render(request, 'accounts/supplier_confirm_delete.html', {'supplier': supplier})