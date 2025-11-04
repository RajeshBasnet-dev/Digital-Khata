from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('create/', views.invoice_create, name='create_invoice'),
    path('<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('<int:invoice_id>/edit/', views.invoice_edit, name='invoice_edit'),
    path('<int:invoice_id>/delete/', views.invoice_delete, name='invoice_delete'),
    path('<int:invoice_id>/print/', views.invoice_print, name='invoice_print'),
]