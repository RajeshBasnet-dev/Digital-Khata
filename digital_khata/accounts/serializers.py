from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Supplier, BusinessProfile, Account, JournalEntry, JournalItem, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        # Set the user from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        # Set the user from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = [
            'id', 'business_name', 'business_type', 'address', 
            'country', 'tax_id', 'currency', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        # Set the user from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'name', 'code', 'account_type', 'opening_balance', 
            'current_balance', 'is_active', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        # Set the user and business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            # Set business from user's business profile
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        return super().create(validated_data)

class JournalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalItem
        fields = ['id', 'account', 'debit', 'credit']

class JournalEntrySerializer(serializers.ModelSerializer):
    items = JournalItemSerializer(many=True)
    
    class Meta:
        model = JournalEntry
        fields = [
            'id', 'date', 'reference_no', 'narration', 
            'items', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # Set the user and business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            # Set business from user's business profile
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        
        journal_entry = JournalEntry.objects.create(**validated_data)
        
        for item_data in items_data:
            JournalItem.objects.create(entry=journal_entry, **item_data)
            
        return journal_entry

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id', 'name', 'category', 'account', 'amount', 
            'date', 'recurrence', 'description', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        # Set the user and business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            # Set business from user's business profile
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        return super().create(validated_data)