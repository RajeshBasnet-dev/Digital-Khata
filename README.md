# Digital Khata - Small Business Management Application

Digital Khata is a Django-based web application designed for small business management, inspired by the Karobar App. It provides essential features for managing sales, purchases, inventory, and financial reporting.

## Features

### User Authentication
- Sign up, login, and logout functionality
- User-specific data isolation (each user sees only their data)

### Dashboard
- Summary of total sales, purchases, outstanding invoices, and stock alerts
- Recent sales overview
- Top products display
- Low stock warnings

### Inventory Management
- CRUD operations for products (name, SKU, price, quantity, tax)
- Automatic stock updates when invoices/bills are created
- Low-stock alerts

### Sales Invoice Management
- Create sales invoices with customer, product, quantity, price, and tax
- Track payment status (paid/unpaid)
- Automatic product quantity deduction

### Purchase/Bill Management
- Record purchases from suppliers
- Track supplier balances
- Automatic product quantity increase

### Reporting
- Daily, weekly, and monthly summaries for sales, purchases, and stock
- Export reports to CSV format

## Technology Stack
- **Backend**: Django 5.2.7 with Python
- **Database**: SQLite (for development)
- **Frontend**: HTML, CSS, JavaScript with Bootstrap 5
- **Authentication**: Django's built-in authentication system

## Installation

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

```
digital_khata/
├── accounts/          # User authentication and customer/supplier management
├── dashboard/         # Dashboard views and templates
├── inventory/         # Product and inventory management
├── sales/             # Sales invoice management
├── purchases/         # Purchase bill management
├── reports/           # Reporting functionality
├── templates/         # HTML templates
├── static/            # CSS, JavaScript, and other static files
├── manage.py          # Django management script
└── digital_khata/     # Main project settings and configuration
```

## Database Models

### Accounts
- **Customer**: Customer information (name, email, phone, address)
- **Supplier**: Supplier information (name, email, phone, address)

### Inventory
- **Product**: Product details (name, SKU, price, quantity, tax rate)

### Sales
- **Invoice**: Sales invoice (customer, date, status, amounts)
- **InvoiceItem**: Individual items in an invoice

### Purchases
- **Bill**: Purchase bill (supplier, date, status, amounts)
- **BillItem**: Individual items in a bill

## URLs

- `/` - Redirects to dashboard
- `/accounts/` - User authentication
- `/dashboard/` - Main dashboard
- `/inventory/` - Product management
- `/sales/` - Sales invoice management
- `/purchases/` - Purchase bill management
- `/reports/` - Financial reporting

## License

This project is open source and available under the MIT License.