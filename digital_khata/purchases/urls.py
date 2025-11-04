from django.urls import path
from . import views

app_name = 'purchases'
urlpatterns = [
    # Traditional views
    path('', views.bill_list, name='bill_list'),
    path('create/', views.bill_create, name='bill_create'),
    path('<int:pk>/update/', views.bill_update, name='bill_update'),
    path('<int:pk>/delete/', views.bill_delete, name='bill_delete'),
    
    # API endpoints
    path('api/bills/', views.BillListCreateAPIView.as_view(), name='bill-list-create'),
    path('api/bills/<int:pk>/', views.BillRetrieveUpdateDestroyAPIView.as_view(), name='bill-detail'),
]