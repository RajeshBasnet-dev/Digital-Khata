from django.db import models
from django.contrib.auth.models import User
from accounts.models import BusinessProfile

class Category(models.Model):
    """Model representing a product category."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('business', 'name')

class Product(models.Model):
    """Model representing a product in inventory."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=10)
    unit = models.CharField(max_length=20, default='piece')
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_stock_status(self):
        """Return stock status based on quantity and threshold."""
        if self.stock_quantity == 0:
            return 'out_of_stock'
        elif self.stock_quantity <= self.low_stock_threshold:
            return 'low_stock'
        else:
            return 'in_stock'

    @property
    def is_low_stock(self):
        """Check if product is low on stock."""
        return self.stock_quantity <= self.low_stock_threshold and self.stock_quantity > 0

    @property
    def is_out_of_stock(self):
        """Check if product is out of stock."""
        return self.stock_quantity == 0