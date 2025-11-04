from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    stock_status = serializers.CharField(source='get_stock_status', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'description', 'price', 'stock_quantity',
            'low_stock_threshold', 'unit', 'tax_rate', 'category', 
            'category_name', 'stock_status', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
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
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        # Update the user and business from the request context if needed
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
        return super().update(instance, validated_data)