from django.contrib import admin
from .models import Customer, Supplier

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'user', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'user')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'user', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'user')