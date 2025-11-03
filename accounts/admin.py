"""
Admin configuration for the accounts app in Digital Khata.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Supplier, BusinessProfile, Account, JournalEntry, JournalItem, Expense

# Register your models here
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Admin configuration for Customer model."""
    list_display = ('name', 'email', 'phone', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin configuration for Supplier model."""
    list_display = ('name', 'email', 'phone', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    """Admin configuration for BusinessProfile model."""
    list_display = ('business_name', 'business_type', 'user', 'country', 'created_at')
    list_filter = ('business_type', 'country', 'created_at')
    search_fields = ('business_name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Admin configuration for Account model."""
    list_display = ('code', 'name', 'account_type', 'business', 'current_balance', 'is_active')
    list_filter = ('account_type', 'is_active', 'business')
    search_fields = ('code', 'name')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    """Admin configuration for JournalEntry model."""
    list_display = ('reference_no', 'date', 'business', 'user')
    list_filter = ('date', 'business')
    search_fields = ('reference_no', 'narration')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(JournalItem)
class JournalItemAdmin(admin.ModelAdmin):
    """Admin configuration for JournalItem model."""
    list_display = ('entry', 'account', 'debit', 'credit')
    list_filter = ('account',)
    search_fields = ('account__name', 'entry__reference_no')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """Admin configuration for Expense model."""
    list_display = ('name', 'category', 'amount', 'date', 'business', 'recurrence')
    list_filter = ('category', 'date', 'recurrence', 'business')
    search_fields = ('name', 'category')
    readonly_fields = ('created_at', 'updated_at')