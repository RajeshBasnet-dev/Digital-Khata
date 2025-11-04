from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    # Traditional views
    path('sales/', views.sales_report, name='sales_report'),
    path('purchases/', views.purchases_report, name='purchases_report'),
    path('inventory/', views.inventory_report, name='inventory_report'),
    path('export/sales/csv/', views.export_sales_csv, name='export_sales_csv'),
    path('export/purchases/csv/', views.export_purchases_csv, name='export_purchases_csv'),
    
    # API endpoints
    path('api/sales/', views.sales_report_data, name='sales-report-data'),
    path('api/purchases/', views.purchases_report_data, name='purchases-report-data'),
    path('api/inventory/', views.inventory_report_data, name='inventory-report-data'),
]