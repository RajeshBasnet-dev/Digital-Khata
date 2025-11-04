from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def business_setup(request):
    """Business setup step"""
    return render(request, 'onboarding/business_setup.html')

@login_required
def add_products(request):
    """Add products step"""
    return render(request, 'onboarding/add_products.html')

@login_required
def create_invoice(request):
    """Create invoice step"""
    context = {
        'today': date.today().strftime('%Y-%m-%d')
    }
    return render(request, 'onboarding/create_invoice.html', context)