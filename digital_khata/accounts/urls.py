from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    # Traditional views
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('business-setup/', views.business_setup, name='business_setup'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/update/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    
    # API endpoints
    path('api/customers/', views.CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    path('api/suppliers/', views.SupplierListCreateAPIView.as_view(), name='supplier-list-create'),
    path('api/suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail'),
    path('api/business-profiles/', views.BusinessProfileListCreateAPIView.as_view(), name='business-profile-list-create'),
    path('api/business-profiles/<int:pk>/', views.BusinessProfileRetrieveUpdateDestroyAPIView.as_view(), name='business-profile-detail'),
    path('api/accounts/', views.AccountListCreateAPIView.as_view(), name='account-list-create'),
    path('api/accounts/<int:pk>/', views.AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-detail'),
    path('api/journal-entries/', views.JournalEntryListCreateAPIView.as_view(), name='journal-entry-list-create'),
    path('api/journal-entries/<int:pk>/', views.JournalEntryRetrieveUpdateDestroyAPIView.as_view(), name='journal-entry-detail'),
    path('api/expenses/', views.ExpenseListCreateAPIView.as_view(), name='expense-list-create'),
    path('api/expenses/<int:pk>/', views.ExpenseRetrieveUpdateDestroyAPIView.as_view(), name='expense-detail'),
    path('api/profile/', views.user_profile, name='user-profile'),
    path('api/logout/', views.logout, name='api-logout'),
]