# Digital Khata

A Django-based small business management web application designed for Nepali businesses.

## Features

- **Inventory Management**: Track products, stock levels, and low-stock alerts
- **Sales & Purchases**: Create invoices and bills with automatic tax calculations
- **Financial Reporting**: Generate reports and export data
- **User Authentication**: Secure login and signup system
- **Responsive Design**: Works on desktop and mobile devices

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License.