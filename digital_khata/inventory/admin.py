from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'quantity', 'tax_rate', 'user', 'created_at')
    search_fields = ('name', 'sku')
    list_filter = ('created_at', 'user')
    list_editable = ('price', 'quantity')