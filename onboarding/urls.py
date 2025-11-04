from django.urls import path
from . import views

app_name = 'onboarding'

urlpatterns = [
    path('business-setup/', views.business_setup, name='business_setup'),
    path('add-products/', views.add_products, name='add_products'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),
]