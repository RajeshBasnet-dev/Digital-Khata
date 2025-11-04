from rest_framework import serializers
from .models import Bill, BillItem
from accounts.models import Supplier
from inventory.models import Product

class BillItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = BillItem
        fields = [
            'id', 'product', 'product_name', 'quantity', 'unit_price', 
            'tax_rate', 'tax_amount', 'total_price'
        ]

class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True)
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    
    class Meta:
        model = Bill
        fields = [
            'id', 'supplier', 'supplier_name', 'date', 'bill_number',
            'subtotal', 'tax_amount', 'tax_rate', 'total_amount',
            'paid_amount', 'due_amount', 'status', 'items',
            'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # Set the user and business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            # Set business from user's business profile
            from accounts.models import BusinessProfile
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        
        bill = Bill.objects.create(**validated_data)
        
        for item_data in items_data:
            BillItem.objects.create(bill=bill, **item_data)
            
        return bill
        
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        
        # Update bill fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update items if provided
        if items_data is not None:
            # Delete existing items
            instance.items.all().delete()
            # Create new items
            for item_data in items_data:
                BillItem.objects.create(bill=instance, **item_data)
                
        return instance