from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category
from .forms import ProductForm
from .serializers import ProductSerializer, CategorySerializer

@login_required
def product_list(request):
    products = Product.objects.filter(user=request.user)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(sku__icontains=search_query)
        )
    
    # Filter by low stock
    low_stock = request.GET.get('low_stock')
    if low_stock:
        products = products.filter(quantity__lte=10)
    
    return render(request, 'inventory/product_list.html', {
        'products': products,
        'search_query': search_query
    })

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product created successfully!')
            return redirect('inventory:product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('inventory:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('inventory:product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})


# API Views
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Set the user and business from the request
        from accounts.models import BusinessProfile
        try:
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            serializer.save(user=self.request.user, business=business_profile)
        except BusinessProfile.DoesNotExist:
            serializer.save(user=self.request.user)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Set the user and business from the request
        from accounts.models import BusinessProfile
        try:
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            serializer.save(user=self.request.user, business=business_profile)
        except BusinessProfile.DoesNotExist:
            serializer.save(user=self.request.user)

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)