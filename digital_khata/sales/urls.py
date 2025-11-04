from django.urls import path
from . import views

app_name = 'sales'
urlpatterns = [
    # Traditional views
    path('', views.invoice_list, name='invoice_list'),
    path('create/', views.invoice_create, name='invoice_create'),
    path('<int:pk>/update/', views.invoice_update, name='invoice_update'),
    path('<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
    
    # API endpoints
    path('api/invoices/', views.InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),
    path('api/invoices/<int:pk>/', views.InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice-detail'),
]