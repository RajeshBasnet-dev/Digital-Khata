from django.urls import path
from . import views

app_name = 'accounting'
urlpatterns = [
    # Traditional views
    path('chart/', views.chart_of_accounts, name='chart_of_accounts'),
    path('journal/', views.journal_entries, name='journal_entries'),
    path('ledger/<int:account_id>/', views.ledger, name='ledger'),
    path('profit-loss/', views.profit_loss, name='profit_loss'),
    path('tax-summary/', views.tax_summary, name='tax_summary'),
    path('expenses/', views.expenses, name='expenses'),
    path('expenses/create/', views.create_expense, name='create_expense'),
    
    # API endpoints
    path('api/tax-configurations/', views.TaxConfigurationListCreateAPIView.as_view(), name='tax-configuration-list-create'),
    path('api/tax-configurations/<int:pk>/', views.TaxConfigurationRetrieveUpdateDestroyAPIView.as_view(), name='tax-configuration-detail'),
    path('api/accounts/', views.AccountListCreateAPIView.as_view(), name='account-list-create'),
    path('api/accounts/<int:pk>/', views.AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-detail'),
    path('api/journal-entries/', views.JournalEntryListCreateAPIView.as_view(), name='journal-entry-list-create'),
    path('api/journal-entries/<int:pk>/', views.JournalEntryRetrieveUpdateDestroyAPIView.as_view(), name='journal-entry-detail'),
    path('api/ledgers/', views.LedgerListAPIView.as_view(), name='ledger-list'),
    path('api/expenses/', views.ExpenseListCreateAPIView.as_view(), name='expense-list-create'),
    path('api/expenses/<int:pk>/', views.ExpenseRetrieveUpdateDestroyAPIView.as_view(), name='expense-detail'),
]