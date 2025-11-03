"""
Utility functions for Digital Khata application.
"""

from django.utils.text import slugify
import random
import string

def generate_invoice_number(prefix='INV'):
    """
    Generate a unique invoice number.
    
    Args:
        prefix (str): Prefix for the invoice number. Defaults to 'INV'.
        
    Returns:
        str: Generated invoice number in format PREFIX-YYYYMMDD-XXXX
    """
    from datetime import datetime
    date_str = datetime.now().strftime('%Y%m%d')
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{prefix}-{date_str}-{random_str}"

def generate_bill_number(prefix='BILL'):
    """
    Generate a unique bill number.
    
    Args:
        prefix (str): Prefix for the bill number. Defaults to 'BILL'.
        
    Returns:
        str: Generated bill number in format PREFIX-YYYYMMDD-XXXX
    """
    from datetime import datetime
    date_str = datetime.now().strftime('%Y%m%d')
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{prefix}-{date_str}-{random_str}"

def generate_sku(product_name, prefix='SKU'):
    """
    Generate a SKU for a product.
    
    Args:
        product_name (str): Name of the product.
        prefix (str): Prefix for the SKU. Defaults to 'SKU'.
        
    Returns:
        str: Generated SKU in format PREFIX-XXXXXX
    """
    # Create a slug from the product name
    slug = slugify(product_name)[:6].upper()
    # Add random characters to ensure uniqueness
    random_str = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}-{slug}-{random_str}"

def format_currency(amount, currency='NPR'):
    """
    Format amount as currency.
    
    Args:
        amount (float): Amount to format.
        currency (str): Currency code. Defaults to 'NPR'.
        
    Returns:
        str: Formatted currency string.
    """
    return f"{currency} {amount:,.2f}"

def calculate_tax(amount, tax_rate):
    """
    Calculate tax amount.
    
    Args:
        amount (float): Base amount.
        tax_rate (float): Tax rate as percentage.
        
    Returns:
        float: Calculated tax amount.
    """
    return amount * (tax_rate / 100)

def calculate_total_with_tax(amount, tax_rate):
    """
    Calculate total amount including tax.
    
    Args:
        amount (float): Base amount.
        tax_rate (float): Tax rate as percentage.
        
    Returns:
        float: Total amount including tax.
    """
    tax_amount = calculate_tax(amount, tax_rate)
    return amount + tax_amount