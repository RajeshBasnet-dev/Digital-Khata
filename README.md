# Digital Khata

A Django-based small business management web application designed for Nepali businesses.

## Features

- **Inventory Management**: Track products, stock levels, and low-stock alerts
- **Sales & Purchases**: Create invoices and bills with automatic tax calculations
- **Financial Reporting**: Generate reports and export data
- **User Authentication**: Secure login and signup system
- **Responsive Design**: Works on desktop and mobile devices
- **Accounting System**: Complete double-entry bookkeeping with chart of accounts
- **Tax Management**: Automatic GST/VAT calculation and reporting
- **Expense Tracking**: Manage business expenses with recurrence options
- **Dashboard Analytics**: Visualize business performance with charts

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Django built-in authentication

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd digital-khata
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Visit `http://127.0.0.1:8000/` to access the landing page
2. Sign up for a new account or log in with existing credentials
3. Set up your business profile
4. Start managing your business operations

## Project Structure

```
karobar_app/
├── digital_khata/          # Main Django project
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI deployment configuration
├── accounts/               # User authentication and business profiles
├── dashboard/              # Main dashboard and analytics
├── inventory/              # Product and inventory management
├── sales/                  # Sales invoices and customers
├── purchases/              # Purchase bills and suppliers
├── reports/                # Business reporting and analytics
├── accounting/             # Double-entry bookkeeping system
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, and image files
└── manage.py              # Django management script
```

## Key Modules

### Accounts
- User registration and authentication
- Business profile management
- Customer and supplier management

### Inventory
- Product catalog management
- Stock level tracking
- Low stock alerts
- Product categories

### Sales
- Invoice creation and management
- Customer records
- Sales reporting

### Purchases
- Bill creation and management
- Supplier records
- Purchase reporting

### Accounting
- Chart of accounts
- Journal entries
- Ledger management
- Tax configuration
- Profit and loss statements

### Reports
- Financial dashboards
- Business analytics
- Exportable reports

## Development

### Creating a Superuser
```bash
python manage.py createsuperuser
```

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License.

## Development Status

This project is actively maintained with regular updates and improvements.

## Developer Information

- **Name**: Rajesh Basnet
- **Email**: basnetrajesh245@gmail.com
- **Phone**: 9749782458
- **LinkedIn**: [Rajesh Basnet](https://www.linkedin.com/in/rajesh-basnet-360188340/)
- **Education**: Bachelor in Management Studies (BMS), Lumbini Banijya Campus