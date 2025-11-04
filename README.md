# Digital Khata - Integrated Django + React Application

This is a business management application built with Django backend and React frontend. The application provides a complete solution for small business accounting, inventory management, sales, purchases, and financial reporting.

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

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

### 2. Frontend Setup (React)

1. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Running the Application

### Development Mode

To run both Django backend and React frontend in development mode:

1. Start the Django backend:
   ```bash
   python manage.py runserver
   ```
   This will start the backend on http://127.0.0.1:8000

2. In a separate terminal, start the React frontend:
   ```bash
   cd frontend
   npm run dev
   ```
   This will start the frontend on http://localhost:3000

The frontend is configured to proxy API requests to the Django backend automatically.

### Production Build

To build the frontend for production:

1. Build the React app:
   ```bash
   cd frontend
   npm run build
   ```

2. The built files will be in the `dist` folder, which Django is configured to serve.

## API Endpoints

All API endpoints are prefixed with `/api/` and require authentication:

### Authentication
- `POST /accounts/api/login/` - User login
- `POST /accounts/api/logout/` - User logout
- `POST /accounts/api/signup/` - User registration
- `GET /accounts/api/profile/` - Get user profile

### Dashboard
- `GET /dashboard/api/data/` - Get dashboard metrics

### Inventory
- `GET /inventory/api/products/` - List all products
- `POST /inventory/api/products/` - Create a new product
- `GET /inventory/api/products/{id}/` - Get a specific product
- `PUT /inventory/api/products/{id}/` - Update a product
- `DELETE /inventory/api/products/{id}/` - Delete a product
- `GET /inventory/api/categories/` - List all categories
- `POST /inventory/api/categories/` - Create a new category
- `GET /inventory/api/categories/{id}/` - Get a specific category
- `PUT /inventory/api/categories/{id}/` - Update a category
- `DELETE /inventory/api/categories/{id}/` - Delete a category

### Sales
- `GET /sales/api/invoices/` - List all invoices
- `POST /sales/api/invoices/` - Create a new invoice
- `GET /sales/api/invoices/{id}/` - Get a specific invoice
- `PUT /sales/api/invoices/{id}/` - Update an invoice
- `DELETE /sales/api/invoices/{id}/` - Delete an invoice

### Purchases
- `GET /purchases/api/bills/` - List all bills
- `POST /purchases/api/bills/` - Create a new bill
- `GET /purchases/api/bills/{id}/` - Get a specific bill
- `PUT /purchases/api/bills/{id}/` - Update a bill
- `DELETE /purchases/api/bills/{id}/` - Delete a bill

### Accounting
- `GET /accounting/api/accounts/` - List all accounts
- `POST /accounting/api/accounts/` - Create a new account
- `GET /accounting/api/accounts/{id}/` - Get a specific account
- `PUT /accounting/api/accounts/{id}/` - Update an account
- `DELETE /accounting/api/accounts/{id}/` - Delete an account
- `GET /accounting/api/journal-entries/` - List all journal entries
- `POST /accounting/api/journal-entries/` - Create a new journal entry
- `GET /accounting/api/journal-entries/{id}/` - Get a specific journal entry
- `PUT /accounting/api/journal-entries/{id}/` - Update a journal entry
- `DELETE /accounting/api/journal-entries/{id}/` - Delete a journal entry
- `GET /accounting/api/ledgers/` - List all ledger entries
- `GET /accounting/api/expenses/` - List all expenses
- `POST /accounting/api/expenses/` - Create a new expense
- `GET /accounting/api/expenses/{id}/` - Get a specific expense
- `PUT /accounting/api/expenses/{id}/` - Update an expense
- `DELETE /accounting/api/expenses/{id}/` - Delete an expense
- `GET /accounting/api/tax-configurations/` - List all tax configurations
- `POST /accounting/api/tax-configurations/` - Create a new tax configuration
- `GET /accounting/api/tax-configurations/{id}/` - Get a specific tax configuration
- `PUT /accounting/api/tax-configurations/{id}/` - Update a tax configuration
- `DELETE /accounting/api/tax-configurations/{id}/` - Delete a tax configuration

### Reports
- `GET /reports/api/sales/` - Get sales report data
- `GET /reports/api/purchases/` - Get purchases report data
- `GET /reports/api/inventory/` - Get inventory report data

## Project Structure

```
karobar_app/
├── digital_khata/          # Django project settings
├── accounts/               # User authentication and profiles
├── dashboard/              # Dashboard views and APIs
├── inventory/              # Product inventory management
├── sales/                  # Sales and invoicing
├── purchases/              # Purchases and bills
├── accounting/             # Accounting and financial records
├── reports/                # Business reports
├── frontend/               # React frontend application
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── start_dev.sh           # Development startup script (Linux/Mac)
└── start_dev.bat          # Development startup script (Windows)
```

## Features

- User authentication (login/signup)
- Business profile setup
- Dashboard with business overview and key metrics
- Inventory management (products, categories, stock tracking)
- Sales management (invoices, customers)
- Purchase management (bills, suppliers)
- Accounting (chart of accounts, journal entries, ledgers)
- Tax management and reporting
- Expense tracking
- Financial reports (sales, purchases, inventory, profit & loss)
- Data export capabilities
- Responsive design for all devices

## Development Scripts

The project includes convenient scripts for development:

### Linux/Mac
```bash
./start_dev.sh
```

### Windows
```cmd
start_dev.bat
```

These scripts will automatically:
1. Set up the Python virtual environment if it doesn't exist
2. Install dependencies
3. Start the Django backend server
4. Start the React frontend development server

## Deployment

For production deployment:

1. Build the frontend:
   ```bash
   cd frontend
   npm run build
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Run the Django server with a production WSGI server like Gunicorn:
   ```bash
   gunicorn digital_khata.wsgi:application
   ```

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