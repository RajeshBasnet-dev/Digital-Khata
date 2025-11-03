"""
Management command to create default chart of accounts for a business.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import BusinessProfile, Account

class Command(BaseCommand):
    """Create default chart of accounts for all businesses."""
    
    help = 'Create default chart of accounts for all businesses'

    def handle(self, *args, **options):
        """Handle the command execution."""
        # Get all business profiles
        businesses = BusinessProfile.objects.all()
        
        if not businesses.exists():
            self.stdout.write(
                self.style.WARNING('No businesses found. Please create a business first.')
            )
            return
        
        # Default accounts to create
        default_accounts = [
            # Assets
            {'code': '1001', 'name': 'Cash', 'account_type': 'asset'},
            {'code': '1002', 'name': 'Bank Account', 'account_type': 'asset'},
            {'code': '1003', 'name': 'Accounts Receivable', 'account_type': 'asset'},
            {'code': '1004', 'name': 'Inventory', 'account_type': 'asset'},
            
            # Liabilities
            {'code': '2001', 'name': 'Accounts Payable', 'account_type': 'liability'},
            {'code': '2002', 'name': 'Loans Payable', 'account_type': 'liability'},
            {'code': '2003', 'name': 'Tax Payable', 'account_type': 'liability'},
            
            # Equity
            {'code': '3001', 'name': 'Owner Equity', 'account_type': 'equity'},
            {'code': '3002', 'name': 'Retained Earnings', 'account_type': 'equity'},
            
            # Income
            {'code': '4001', 'name': 'Sales Revenue', 'account_type': 'income'},
            {'code': '4002', 'name': 'Service Revenue', 'account_type': 'income'},
            
            # Expenses
            {'code': '5001', 'name': 'Cost of Goods Sold', 'account_type': 'expense'},
            {'code': '5002', 'name': 'Rent Expense', 'account_type': 'expense'},
            {'code': '5003', 'name': 'Utilities Expense', 'account_type': 'expense'},
            {'code': '5004', 'name': 'Salaries Expense', 'account_type': 'expense'},
            {'code': '5005', 'name': 'Marketing Expense', 'account_type': 'expense'},
        ]
        
        created_count = 0
        
        # Create accounts for each business
        for business in businesses:
            user = business.user
            self.stdout.write(
                f'Creating accounts for business: {business.business_name}'
            )
            
            for account_data in default_accounts:
                # Check if account already exists
                account, created = Account.objects.get_or_create(
                    business=business,
                    code=account_data['code'],
                    defaults={
                        'user': user,
                        'name': account_data['name'],
                        'account_type': account_data['account_type'],
                        'is_active': True
                    }
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(
                        f'  Created account: {account.code} - {account.name}'
                    )
                else:
                    self.stdout.write(
                        f'  Account already exists: {account.code} - {account.name}'
                    )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} accounts across {businesses.count()} businesses'
            )
        )