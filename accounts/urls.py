"""
URL configuration for the accounts app in Digital Khata.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    
    # Business setup
    path('business-setup/', views.business_setup, name='business_setup'),
    
    # User profile
    path('profile/', views.profile, name='profile'),
]