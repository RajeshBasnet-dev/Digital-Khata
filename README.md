# Digital Khata - Business Management System

Digital Khata is a comprehensive business management solution built with Django backend and a modern HTML/CSS/JavaScript frontend. The application provides a complete solution for small business accounting, inventory management, sales, purchases, and financial reporting with a professional, responsive UI.

## Features

- **User Authentication**: Secure login and signup system
- **Business Profile Setup**: Configure business details and preferences
- **Dashboard**: Overview of key business metrics and performance indicators
- **Inventory Management**: Track products, categories, and stock levels
- **Sales Management**: Create and manage invoices and customer records
- **Purchase Management**: Handle supplier bills and purchase orders
- **Accounting**: Chart of accounts, journal entries, ledgers, and tax management
- **Financial Reports**: Generate sales, purchase, inventory, and profit/loss reports
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Professional interface with intuitive navigation

## Prerequisites

- Python 3.8+
- Node.js 14+ (for development tools)

## Setup Instructions

### 1. Backend Setup (Django)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

### 2. Frontend Setup (HTML/CSS/JavaScript)

The frontend is built with pure HTML, CSS, and JavaScript with Bootstrap 5 for styling. No build step is required for development.

## Running the Application

### Development Mode

To run the Django application:

```bash
python manage.py runserver
```

This will start the application on http://127.0.0.1:8000

The application includes both the landing page and all business management features in a single Django project.

### Production Deployment

For production deployment:

1. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

2. Run the Django server with a production WSGI server like Gunicorn:
   ```bash
   gunicorn digital_khata.wsgi:application
   ```

## Project Structure

```
karobar_app/
├── digital_khata/          # Django project settings
├── accounts/               # User authentication and profiles
├── dashboard/              # Dashboard views and templates
├── inventory/              # Product inventory management
├── sales/                  # Sales and invoicing
├── purchases/              # Purchases and bills
├── accounting/             # Accounting and financial records
├── reports/                # Business reports
├── frontend/               # HTML templates and static assets
│   ├── templates/          # Django HTML templates
│   └── static/             # CSS, JavaScript, and images
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── start_dev.sh           # Development startup script (Linux/Mac)
└── start_dev.bat          # Development startup script (Windows)
```

## Key Modules

### Authentication
- User registration and login
- Business profile setup
- Session management

### Dashboard
- Business overview with key metrics
- Recent transactions display
- Quick access to frequently used features

### Inventory
- Product management (CRUD operations)
- Stock level tracking
- Low stock alerts
- Product categorization

### Sales
- Invoice creation and management
- Customer records
- Payment tracking
- Sales reporting

### Purchases
- Supplier bill management
- Purchase order tracking
- Supplier records
- Payment status monitoring

### Accounting
- Chart of accounts
- Journal entries
- General ledger
- Tax configuration and reporting
- Profit and loss statements

### Reports
- Sales performance reports
- Purchase analysis
- Inventory status reports
- Financial summaries

## Development

### Templates
All HTML templates are located in `frontend/templates/` and organized by module:
- `accounts/` - Authentication and user profile pages
- `dashboard/` - Dashboard views
- `inventory/` - Product management pages
- `sales/` - Invoice and customer pages
- `purchases/` - Bill and supplier pages
- `accounting/` - Accounting feature pages
- `reports/` - Report generation pages

### Static Assets
CSS, JavaScript, and image files are located in `frontend/static/`:
- `css/` - Custom stylesheets
- `js/` - JavaScript files
- `images/` - Image assets

### Customization
To customize the application:
1. Modify templates in `frontend/templates/`
2. Update styles in `frontend/static/css/style.css`
3. Add JavaScript functionality in `frontend/static/js/main.js`

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Author

Rajesh Basnet
- Email: basnetrajesh245@gmail.com
- Phone: 9749782458
- LinkedIn: https://www.linkedin.com/in/rajesh-basnet-360188340/
- Education: Bachelor in Management Studies (BMS), Lumbini Banijya Campus