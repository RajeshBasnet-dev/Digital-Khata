from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sales.models import Invoice
from purchases.models import Bill
from inventory.models import Product
from django.db.models import Sum, Count, Q
from datetime import datetime, timedelta
import csv
from django.http import HttpResponse

@login_required
def sales_report(request):
    invoices = Invoice.objects.filter(user=request.user)
    
    # Date filters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if start_date and end_date:
        invoices = invoices.filter(date__range=[start_date, end_date])
    
    # Calculate totals
    total_sales = invoices.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_tax = invoices.aggregate(Sum('tax_total'))['tax_total__sum'] or 0
    invoice_count = invoices.count()
    
    # Group by status
    paid_invoices = invoices.filter(status='paid').count()
    unpaid_invoices = invoices.filter(status='unpaid').count()
    
    context = {
        'invoices': invoices,
        'total_sales': total_sales,
        'total_tax': total_tax,
        'invoice_count': invoice_count,
        'paid_invoices': paid_invoices,
        'unpaid_invoices': unpaid_invoices,
        'start_date': start_date,
        'end_date': end_date,
    }
    
    return render(request, 'reports/sales_report.html', context)

@login_required
def purchases_report(request):
    bills = Bill.objects.filter(user=request.user)
    
    # Date filters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if start_date and end_date:
        bills = bills.filter(date__range=[start_date, end_date])
    
    # Calculate totals
    total_purchases = bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_tax = bills.aggregate(Sum('tax_total'))['tax_total__sum'] or 0
    bill_count = bills.count()
    
    # Group by status
    paid_bills = bills.filter(status='paid').count()
    unpaid_bills = bills.filter(status='unpaid').count()
    
    context = {
        'bills': bills,
        'total_purchases': total_purchases,
        'total_tax': total_tax,
        'bill_count': bill_count,
        'paid_bills': paid_bills,
        'unpaid_bills': unpaid_bills,
        'start_date': start_date,
        'end_date': end_date,
    }
    
    return render(request, 'reports/purchases_report.html', context)

@login_required
def inventory_report(request):
    products = Product.objects.filter(user=request.user)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(sku__icontains=search_query)
        )
    
    # Low stock filter
    low_stock = request.GET.get('low_stock')
    if low_stock:
        products = products.filter(quantity__lte=10)
    
    # Calculate inventory value
    total_inventory_value = sum([p.total_value for p in products])
    
    context = {
        'products': products,
        'total_inventory_value': total_inventory_value,
        'search_query': search_query,
    }
    
    return render(request, 'reports/inventory_report.html', context)

@login_required
def export_sales_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_report.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Invoice Number', 'Customer', 'Date', 'Total Amount', 'Status'])
    
    invoices = Invoice.objects.filter(user=request.user)
    for invoice in invoices:
        writer.writerow([
            invoice.invoice_number,
            invoice.customer.name,
            invoice.date,
            invoice.total_amount,
            invoice.status
        ])
    
    return response

@login_required
def export_purchases_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="purchases_report.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Bill Number', 'Supplier', 'Date', 'Total Amount', 'Status'])
    
    bills = Bill.objects.filter(user=request.user)
    for bill in bills:
        writer.writerow([
            bill.bill_number,
            bill.supplier.name,
            bill.date,
            bill.total_amount,
            bill.status
        ])
    
    return response