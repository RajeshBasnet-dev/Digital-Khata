from django.contrib import admin
from .models import Bill, BillItem

class BillItemInline(admin.TabularInline):
    model = BillItem
    extra = 1

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('bill_number', 'supplier', 'date', 'total_amount', 'status', 'user')
    search_fields = ('bill_number', 'supplier__name')
    list_filter = ('status', 'date', 'user')
    inlines = [BillItemInline]

@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = ('bill', 'product', 'quantity', 'unit_price', 'total_price')
    search_fields = ('bill__bill_number', 'product__name')