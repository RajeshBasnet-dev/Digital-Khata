"""
Test cases for Digital Khata views.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationViewTest(TestCase):
    """Test cases for authentication views."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_landing_page_access(self):
        """Test access to landing page."""
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Digital Khata')
    
    def test_login_page_access(self):
        """Test access to login page."""
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome Back')
    
    def test_signup_page_access(self):
        """Test access to signup page."""
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Account')
    
    def test_user_login(self):
        """Test user login functionality."""
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        # Should redirect after successful login
        self.assertEqual(response.status_code, 302)
    
    def test_user_login_invalid_credentials(self):
        """Test login with invalid credentials."""
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        # Should stay on login page with error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

class DashboardViewTest(TestCase):
    """Test cases for dashboard views."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_dashboard_access_authenticated(self):
        """Test dashboard access for authenticated user."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard')
    
    def test_dashboard_access_unauthenticated(self):
        """Test dashboard access for unauthenticated user."""
        response = self.client.get(reverse('dashboard:dashboard'))
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)