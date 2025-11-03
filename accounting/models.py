from django.db import models
from django.contrib.auth.models import User

class TaxConfiguration(models.Model):
    business = models.ForeignKey('accounts.BusinessProfile', on_delete=models.CASCADE)
    tax_name = models.CharField(max_length=50, default='GST')
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=13.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tax_name} - {self.tax_rate}%"

class Ledger(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    date = models.DateField()
    reference_no = models.CharField(max_length=50)
    narration = models.TextField()
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.name} - {self.date}"

    class Meta:
        ordering = ['date', 'created_at']