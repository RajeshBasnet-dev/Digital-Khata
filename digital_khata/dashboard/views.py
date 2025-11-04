from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from sales import models as sales_models
from purchases import models as purchases_models
from inventory import models as inventory_models
from django.db.models import Sum, Count
from datetime import datetime, timedelta


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):
    # Get user-specific data
    invoices = sales_models.Invoice.objects.filter(user=request.user)
    bills = purchases_models.Bill.objects.filter(user=request.user)
    products = inventory_models.Product.objects.filter(user=request.user)
    
    # Calculate totals
    total_sales = float(invoices.aggregate(Sum('total_amount'))['total_amount__sum'] or 0)
    total_purchases = float(bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0)
    total_products = products.count()
    
    # Outstanding invoices (unpaid)
    outstanding_invoices = invoices.filter(status='unpaid').count()
    
    # Low stock products
    low_stock_products = products.filter(quantity__lte=10).count()
    
    # Recent invoices (last 30 days)
    thirty_days_ago = datetime.now().date() - timedelta(days=30)
    recent_invoices = invoices.filter(date__gte=thirty_days_ago).count()
    
    # Recent bills (last 30 days)
    recent_bills = bills.filter(date__gte=thirty_days_ago).count()
    
    # Top selling products (simplified)
    top_products = list(products.order_by('-quantity')[:5].values(
        'id', 'name', 'quantity', 'price'
    ))
    
    data = {
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'total_products': total_products,
        'outstanding_invoices': outstanding_invoices,
        'low_stock_products': low_stock_products,
        'recent_invoices': recent_invoices,
        'recent_bills': recent_bills,
        'top_products': top_products,
    }
    
    return Response(data)

@login_required
def dashboard(request):
    # Get user-specific data
    invoices = sales_models.Invoice.objects.filter(user=request.user)
    bills = purchases_models.Bill.objects.filter(user=request.user)
    products = inventory_models.Product.objects.filter(user=request.user)
    
    # Calculate totals
    total_sales = invoices.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_purchases = bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_products = products.count()
    
    # Outstanding invoices (unpaid)
    outstanding_invoices = invoices.filter(status='unpaid').count()
    
    # Low stock products
    low_stock_products = products.filter(quantity__lte=10).count()
    
    # Recent invoices (last 30 days)
    thirty_days_ago = datetime.now().date() - timedelta(days=30)
    recent_invoices = invoices.filter(date__gte=thirty_days_ago).order_by('-date')
    
    # Top selling products (simplified - would need more complex logic in real app)
    top_products = products.order_by('-quantity')[:5]
    
    context = {
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'total_products': total_products,
        'outstanding_invoices': outstanding_invoices,
        'low_stock_products': low_stock_products,
        'recent_invoices': recent_invoices,
        'top_products': top_products,
    }
    
    return render(request, 'dashboard/dashboard.html', context)