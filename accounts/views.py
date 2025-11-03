"""
Views for the accounts app in Digital Khata.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, BusinessProfileForm
from .models import BusinessProfile

def signup(request):
    """Handle user signup."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('accounts:business_setup')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def business_setup(request):
    """Handle business profile setup."""
    # Check if user already has a business profile
    try:
        business_profile = BusinessProfile.objects.get(user=request.user)
        # If exists, redirect to dashboard
        return redirect('dashboard:dashboard')
    except BusinessProfile.DoesNotExist:
        # If not exists, continue with setup
        pass
    
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST)
        if form.is_valid():
            business_profile = form.save(commit=False)
            business_profile.user = request.user
            business_profile.save()
            messages.success(request, 'Business profile created successfully!')
            return redirect('dashboard:dashboard')
    else:
        form = BusinessProfileForm()
    
    return render(request, 'accounts/business_setup.html', {'form': form})

@login_required
def profile(request):
    """Display user profile."""
    try:
        business_profile = BusinessProfile.objects.get(user=request.user)
    except BusinessProfile.DoesNotExist:
        business_profile = None
    
    context = {
        'business_profile': business_profile
    }
    return render(request, 'accounts/profile.html', context)