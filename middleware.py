"""
Custom middleware for Digital Khata application.
"""

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class BusinessProfileMiddleware:
    """
    Middleware to ensure users have a business profile.
    
    Redirects users to business setup page if they try to access
    protected pages without a business profile.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that don't require business profile
        exempt_urls = [
            reverse('accounts:business_setup'),
            reverse('accounts:logout'),
            reverse('landing'),
        ]
        
        # Add admin URLs to exempt list
        if request.path.startswith('/admin/'):
            exempt_urls.append(request.path)
        
        # Check if user is authenticated and trying to access protected pages
        if (request.user.is_authenticated and 
            not request.path in exempt_urls and
            not request.path.startswith('/admin/')):
            
            # Check if user has business profile
            try:
                request.user.businessprofile
            except AttributeError:
                # Redirect to business setup
                messages.warning(request, 'Please set up your business profile first.')
                return redirect('accounts:business_setup')
        
        response = self.get_response(request)
        return response