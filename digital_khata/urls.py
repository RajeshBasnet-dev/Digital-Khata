"""
URL configuration for digital_khata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inventory/', include('inventory.urls')),
    path('sales/', include('sales.urls')),
    path('purchases/', include('purchases.urls')),
    path('reports/', include('reports.urls')),
    path('accounting/', include('accounting.urls')),
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
]

# Serve frontend build in production
if not settings.DEBUG:
    from django.views.generic import TemplateView
    urlpatterns += [re_path(r'^(?!api|admin|static|media).*$', TemplateView.as_view(template_name='index.html'))]