"""
Test script for Digital Khata application
"""
import os
import sys

def test_project_structure():
    """
    Test basic project structure of the Digital Khata application
    """
    print("Testing Digital Khata project structure...")
    
    # Check that required directories exist
    required_dirs = [
        'digital_khata',
        'digital_khata/accounts',
        'digital_khata/dashboard',
        'digital_khata/inventory',
        'digital_khata/sales',
        'digital_khata/purchases',
        'digital_khata/reports',
        'templates',
        'static'
    ]
    
    print("Checking required directories...")
    for directory in required_dirs:
        assert os.path.exists(directory), f"Directory {directory} does not exist"
        print(f"✓ {directory} exists")
    
    # Check that required files exist
    required_files = [
        'manage.py',
        'digital_khata/settings.py',
        'digital_khata/urls.py',
        'requirements.txt'
    ]
    
    print("Checking required files...")
    for file in required_files:
        assert os.path.exists(file), f"File {file} does not exist"
        print(f"✓ {file} exists")
    
    # Check that apps have models.py
    apps = ['accounts', 'dashboard', 'inventory', 'sales', 'purchases', 'reports']
    print("Checking app structure...")
    for app in apps:
        models_file = f'digital_khata/{app}/models.py'
        views_file = f'digital_khata/{app}/views.py'
        assert os.path.exists(models_file), f"Models file for {app} does not exist"
        assert os.path.exists(views_file), f"Views file for {app} does not exist"
        print(f"✓ {app} has models and views")
    
    print("\nAll structure tests passed! Digital Khata project is properly structured.")
    return True

if __name__ == "__main__":
    try:
        test_project_structure()
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)