"""
URL configuration for digital_khata project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from frontend import views as frontend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend_views.home, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('purchases/', include('purchases.urls', namespace='purchases')),
    path('accounting/', include('accounting.urls', namespace='accounting')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('pricing/', TemplateView.as_view(template_name='pricing.html'), name='pricing'),
    path('onboarding/', include('onboarding.urls', namespace='onboarding')),
]