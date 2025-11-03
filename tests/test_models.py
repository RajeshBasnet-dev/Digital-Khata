"""
Test cases for Digital Khata models.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Customer, Supplier, BusinessProfile

class CustomerModelTest(TestCase):
    """Test cases for the Customer model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.customer = Customer.objects.create(
            user=self.user,
            name='Test Customer',
            email='customer@test.com',
            phone='1234567890'
        )
    
    def test_customer_str_representation(self):
        """Test the string representation of Customer."""
        self.assertEqual(str(self.customer), 'Test Customer')
    
    def test_customer_creation(self):
        """Test customer creation."""
        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.name, 'Test Customer')

class SupplierModelTest(TestCase):
    """Test cases for the Supplier model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.supplier = Supplier.objects.create(
            user=self.user,
            name='Test Supplier',
            email='supplier@test.com',
            phone='0987654321'
        )
    
    def test_supplier_str_representation(self):
        """Test the string representation of Supplier."""
        self.assertEqual(str(self.supplier), 'Test Supplier')
    
    def test_supplier_creation(self):
        """Test supplier creation."""
        self.assertIsInstance(self.supplier, Supplier)
        self.assertEqual(self.supplier.name, 'Test Supplier')

class BusinessProfileModelTest(TestCase):
    """Test cases for the BusinessProfile model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.business = BusinessProfile.objects.create(
            user=self.user,
            business_name='Test Business',
            business_type='retail',
            address='Test Address',
            country='NP',
            tax_id='123456789',
            currency='NPR'
        )
    
    def test_business_str_representation(self):
        """Test the string representation of BusinessProfile."""
        expected = f"Test Business - {self.user.username}"
        self.assertEqual(str(self.business), expected)
    
    def test_business_creation(self):
        """Test business profile creation."""
        self.assertIsInstance(self.business, BusinessProfile)
        self.assertEqual(self.business.business_name, 'Test Business')