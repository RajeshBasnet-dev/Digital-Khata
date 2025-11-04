from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date

def home(request):
    """Render the landing page"""
    return render(request, 'landing.html')

@login_required
def invoice_create(request):
    """Render the invoice creation page"""
    context = {
        'today': date.today().strftime('%Y-%m-%d')
    }
    return render(request, 'invoice_create.html', context)