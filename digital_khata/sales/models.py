from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer, BusinessProfile
from inventory.models import Product

def get_default_business():
    """
    Get or create a default business profile for foreign key defaults
    """
    try:
        # Try to get the first business profile
        return BusinessProfile.objects.first().id
    except:
        # If no business profile exists, create a default one
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            user = User.objects.first()
            if not user:
                user = User.objects.create_user(username='default_user', password='default_password')
            
            business, created = BusinessProfile.objects.get_or_create(
                user=user,
                business_name='Default Business',
                defaults={
                    'business_type': 'retail',
                    'address': 'Default Address',
                    'country': 'NP',
                    'currency': 'NPR'
                }
            )
            return business.id
        except:
            # If all else fails, return 1 (this will cause an error if ID 1 doesn't exist,
            # but Django migrations will handle this appropriately)
            return 1

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, default=get_default_business)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    invoice_number = models.CharField(max_length=50, unique=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled')
    ], default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer.name}"

    def save(self, *args, **kwargs):
        # Calculate due amount
        self.due_amount = float(self.total_amount) - float(self.paid_amount)
        super().save(*args, **kwargs)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} x {self.unit_price}"

    def save(self, *args, **kwargs):
        # Calculate tax amount and total price
        amount = float(self.unit_price) * int(self.quantity)
        self.tax_amount = amount * float(self.tax_rate) / 100
        self.total_price = amount + float(self.tax_amount)
        super().save(*args, **kwargs)