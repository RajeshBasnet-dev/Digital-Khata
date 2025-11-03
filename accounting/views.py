from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from django.http import JsonResponse
from .models import TaxConfiguration, Ledger
from accounts.models import BusinessProfile, Account, JournalEntry, JournalItem
from inventory.models import Product
from sales.models import Invoice, InvoiceItem
from purchases.models import Bill, BillItem
import json
from datetime import datetime, timedelta

@login_required
def chart_of_accounts(request):
    business = get_object_or_404(BusinessProfile, user=request.user)
    accounts = Account.objects.filter(business=business).order_by('code')
    
    if request.method == 'POST':
        # Handle account creation
        name = request.POST.get('name')
        code = request.POST.get('code')
        account_type = request.POST.get('account_type')
        opening_balance = request.POST.get('opening_balance', 0)
        
        try:
            Account.objects.create(
                user=request.user,
                business=business,
                name=name,
                code=code,
                account_type=account_type,
                opening_balance=opening_balance,
                current_balance=opening_balance
            )
            messages.success(request, 'Account created successfully!')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
        
        return redirect('accounting:chart_of_accounts')
    
    context = {
        'accounts': accounts,
        'business': business
    }
    return render(request, 'accounting/chart_of_accounts.html', context)

@login_required
def journal_entries(request):
    business = get_object_or_404(BusinessProfile, user=request.user)
    entries = JournalEntry.objects.filter(business=business).order_by('-date', '-created_at')
    
    context = {
        'entries': entries,
        'business': business
    }
    return render(request, 'accounting/journal_entries.html', context)

@login_required
def ledger(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    business = get_object_or_404(BusinessProfile, user=request.user)
    
    # Get ledger entries for this account
    ledger_entries = Ledger.objects.filter(account=account).order_by('date')
    
    # Calculate running balance
    running_balance = account.opening_balance
    for entry in ledger_entries:
        running_balance += entry.debit - entry.credit
        entry.running_balance = running_balance
    
    context = {
        'account': account,
        'ledger_entries': ledger_entries,
        'business': business
    }
    return render(request, 'accounting/ledger.html', context)

@login_required
def profit_loss(request):
    business = get_object_or_404(BusinessProfile, user=request.user)
    
    # Get date range from request or use default (last 30 days)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)
    
    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), '%Y-%m-%d').date()
    if request.GET.get('end_date'):
        end_date = datetime.strptime(request.GET.get('end_date'), '%Y-%m-%d').date()
    
    # Get income accounts
    income_accounts = Account.objects.filter(
        business=business,
        account_type='income'
    )
    
    # Get expense accounts
    expense_accounts = Account.objects.filter(
        business=business,
        account_type='expense'
    )
    
    # Calculate totals
    total_income = 0
    total_expenses = 0
    
    income_data = []
    for account in income_accounts:
        # Calculate total credit (income) for this account in the date range
        total = Ledger.objects.filter(
            account=account,
            date__range=[start_date, end_date],
            credit__gt=0
        ).aggregate(total=Sum('credit'))['total'] or 0
        
        if total > 0:
            income_data.append({
                'account': account,
                'total': total
            })
            total_income += total
    
    expense_data = []
    for account in expense_accounts:
        # Calculate total debit (expense) for this account in the date range
        total = Ledger.objects.filter(
            account=account,
            date__range=[start_date, end_date],
            debit__gt=0
        ).aggregate(total=Sum('debit'))['total'] or 0
        
        if total > 0:
            expense_data.append({
                'account': account,
                'total': total
            })
            total_expenses += total
    
    net_profit = total_income - total_expenses
    
    context = {
        'business': business,
        'start_date': start_date,
        'end_date': end_date,
        'income_data': income_data,
        'expense_data': expense_data,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_profit': net_profit
    }
    return render(request, 'accounting/profit_loss.html', context)

@login_required
def tax_summary(request):
    business = get_object_or_404(BusinessProfile, user=request.user)
    
    # Get date range from request or use default (last 30 days)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)
    
    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), '%Y-%m-%d').date()
    if request.GET.get('end_date'):
        end_date = datetime.strptime(request.GET.get('end_date'), '%Y-%m-%d').date()
    
    # Get tax configuration
    try:
        tax_config = TaxConfiguration.objects.get(business=business)
    except TaxConfiguration.DoesNotExist:
        # Create default tax configuration if it doesn't exist
        tax_config = TaxConfiguration.objects.create(
            business=business,
            tax_name='GST',
            tax_rate=13.00
        )
    
    # Calculate tax collected from sales
    sales_tax_collected = 0
    sales = Invoice.objects.filter(
        business=business,
        date__range=[start_date, end_date]
    )
    
    for sale in sales:
        sales_tax_collected += float(sale.tax_amount or 0)
    
    # Calculate tax paid on purchases
    purchase_tax_paid = 0
    purchases = Bill.objects.filter(
        business=business,
        date__range=[start_date, end_date]
    )
    
    for purchase in purchases:
        purchase_tax_paid += float(purchase.tax_amount or 0)
    
    # Calculate net tax payable
    net_tax_payable = sales_tax_collected - purchase_tax_paid
    
    context = {
        'business': business,
        'tax_config': tax_config,
        'start_date': start_date,
        'end_date': end_date,
        'sales_tax_collected': sales_tax_collected,
        'purchase_tax_paid': purchase_tax_paid,
        'net_tax_payable': net_tax_payable
    }
    return render(request, 'accounting/tax_summary.html', context)

@login_required
def expenses(request):
    business = get_object_or_404(BusinessProfile, user=request.user)
    expenses = Expense.objects.filter(business=business).order_by('-date')
    
    # Get expense categories for filter
    categories = Expense.objects.filter(business=business).values_list('category', flat=True).distinct()
    
    # Apply category filter if provided
    category_filter = request.GET.get('category')
    if category_filter:
        expenses = expenses.filter(category=category_filter)
    
    context = {
        'expenses': expenses,
        'categories': categories,
        'category_filter': category_filter,
        'business': business
    }
    return render(request, 'accounting/expenses.html', context)

@login_required
def create_expense(request):
    business = get_object_or_404(BusinessProfile, user=request.user)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        account_id = request.POST.get('account')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        recurrence = request.POST.get('recurrence', 'none')
        description = request.POST.get('description', '')
        
        try:
            account = Account.objects.get(id=account_id, business=business)
            Expense.objects.create(
                user=request.user,
                business=business,
                name=name,
                category=category,
                account=account,
                amount=amount,
                date=date,
                recurrence=recurrence,
                description=description
            )
            messages.success(request, 'Expense created successfully!')
        except Exception as e:
            messages.error(request, f'Error creating expense: {str(e)}')
        
        return redirect('accounting:expenses')
    
    # Get accounts for dropdown
    accounts = Account.objects.filter(business=business)
    
    context = {
        'accounts': accounts,
        'business': business
    }
    return render(request, 'accounting/create_expense.html', context)