from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, CustomerForm, SupplierForm, BusinessProfileForm
from .models import Customer, Supplier, BusinessProfile, Account, JournalEntry, Expense

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .serializers import (
    UserSerializer, CustomerSerializer, SupplierSerializer, 
    BusinessProfileSerializer, AccountSerializer, JournalEntrySerializer, 
    ExpenseSerializer
)


# API Views
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

class SupplierListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)

class BusinessProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return BusinessProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BusinessProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return BusinessProfile.objects.filter(user=self.request.user)

class AccountListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Set business from user's business profile
        try:
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            serializer.save(user=self.request.user, business=business_profile)
        except BusinessProfile.DoesNotExist:
            serializer.save(user=self.request.user)

class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

class JournalEntryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Set business from user's business profile
        try:
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            serializer.save(user=self.request.user, business=business_profile)
        except BusinessProfile.DoesNotExist:
            serializer.save(user=self.request.user)

class JournalEntryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

class ExpenseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Set business from user's business profile
        try:
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            serializer.save(user=self.request.user, business=business_profile)
        except BusinessProfile.DoesNotExist:
            serializer.save(user=self.request.user)

class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    # Django's logout functionality
    from django.contrib.auth import logout
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

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