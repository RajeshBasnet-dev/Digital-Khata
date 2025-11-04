from django.db import models
from django.contrib.auth.models import User
from accounts.models import BusinessProfile, Account

class TaxConfiguration(models.Model):
    """Model representing tax configuration for a business."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    tax_name = models.CharField(max_length=50, default='VAT')
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=13.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tax_name} ({self.tax_rate}%)"

class Ledger(models.Model):
    """Model representing a ledger entry for account transactions."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    reference_no = models.CharField(max_length=50)
    narration = models.TextField()
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'created_at']

    def __str__(self):
        return f"{self.account.name} - {self.date}"