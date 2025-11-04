from rest_framework import serializers
from .models import TaxConfiguration, Ledger
from accounts.models import BusinessProfile, Account, JournalEntry, JournalItem, Expense

class TaxConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxConfiguration
        fields = ['id', 'tax_name', 'tax_rate', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        # Set the business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
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
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        return super().create(validated_data)

class JournalItemSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    
    class Meta:
        model = JournalItem
        fields = ['id', 'account', 'account_name', 'debit', 'credit', 'created_at']

class JournalEntrySerializer(serializers.ModelSerializer):
    items = JournalItemSerializer(many=True)
    business_name = serializers.CharField(source='business.business_name', read_only=True)
    
    class Meta:
        model = JournalEntry
        fields = [
            'id', 'date', 'reference_no', 'narration', 'business', 
            'business_name', 'items', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # Set the user and business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        
        journal_entry = JournalEntry.objects.create(**validated_data)
        
        for item_data in items_data:
            JournalItem.objects.create(entry=journal_entry, **item_data)
            
        return journal_entry
        
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        
        # Update journal entry fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update items if provided
        if items_data is not None:
            # Delete existing items
            instance.items.all().delete()
            # Create new items
            for item_data in items_data:
                JournalItem.objects.create(entry=instance, **item_data)
                
        return instance

class LedgerSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    
    class Meta:
        model = Ledger
        fields = [
            'id', 'account', 'account_name', 'date', 'description', 
            'debit', 'credit', 'created_at'
        ]

class ExpenseSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    
    class Meta:
        model = Expense
        fields = [
            'id', 'name', 'category', 'account', 'account_name', 'amount', 
            'date', 'recurrence', 'description', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        # Set the user and business from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
            try:
                business_profile = BusinessProfile.objects.get(user=request.user)
                validated_data['business'] = business_profile
            except BusinessProfile.DoesNotExist:
                pass
        return super().create(validated_data)