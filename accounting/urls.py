from django.urls import path
from . import views

app_name = 'accounting'
urlpatterns = [
    path('chart/', views.chart_of_accounts, name='chart_of_accounts'),
    path('journal/', views.journal_entries, name='journal_entries'),
    path('ledger/<int:account_id>/', views.ledger, name='ledger'),
    path('profit-loss/', views.profit_loss, name='profit_loss'),
    path('tax-summary/', views.tax_summary, name='tax_summary'),
    path('expenses/', views.expenses, name='expenses'),
    path('expenses/create/', views.create_expense, name='create_expense'),
]