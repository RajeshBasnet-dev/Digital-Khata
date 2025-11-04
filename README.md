# Digital Khata - Smart Business Management System

Digital Khata is a comprehensive business management solution designed specifically for small shop owners in emerging markets. It helps manage inventory, track sales, handle purchases, maintain accounting records, and generate insightful reports - all in one place.

## Features

### 📊 Dashboard
- Real-time business overview
- Key performance indicators
- Recent transactions
- Quick action buttons

### 📦 Inventory Management
- Product catalog with categories
- Stock level tracking
- Low stock alerts
- Supplier management

### 💰 Sales Management
- Invoice creation and tracking
- Customer management
- Payment tracking
- Sales history

### 🛒 Purchase Management
- Supplier bill tracking
- Purchase order management
- Payment status tracking

### 📈 Accounting
- Chart of accounts
- Transaction recording
- Financial reporting
- Profit & loss statements

### 📊 Reports & Analytics
- Sales reports
- Inventory reports
- Customer insights
- Performance metrics

## Tech Stack

### Backend
- **Python 3.8+**
- **Django 4.x**
- **Django REST Framework**
- **SQLite** (development) / **PostgreSQL** (production)

### Frontend
- **Tailwind CSS** - Modern utility-first CSS framework
- **Bootstrap Icons** - Icon library
- **Vanilla JavaScript** - No frameworks, lightweight and fast
- **Responsive Design** - Works on all devices

### Deployment
- **Docker** (optional)
- **Gunicorn** - WSGI HTTP Server
- **Nginx** (production)
- **WhiteNoise** - Static file serving

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/digital-khata.git
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

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application at `http://localhost:8000`
2. Sign up for a new account or log in with your superuser credentials
3. Start managing your business!

## Premium UI Features

### Modern Design System
- Clean, professional interface with Tailwind CSS
- Responsive layout that works on mobile, tablet, and desktop
- Intuitive navigation and user experience
- Dark mode support

### Component Library
- Premium buttons with hover effects
- Interactive cards with subtle animations
- Custom form elements with validation
- Data tables with sorting and filtering
- Modal dialogs for actions
- Toast notifications for feedback
- Loading skeletons for better perceived performance
- Empty states for better UX

### Conversion Optimization
- Freemium model with clear upgrade paths
- In-app upgrade prompts
- PWA support for offline access
- WhatsApp integration for sharing
- Success animations for positive feedback

### Performance
- Optimized for low-end devices
- Fast loading times (< 300ms FCP)
- Minimal external dependencies
- Service worker for caching

## Project Structure

```
digital-khata/
├── accounts/              # User authentication and profiles
├── inventory/             # Product and stock management
├── sales/                 # Invoice and customer management
├── purchases/             # Supplier and bill management
├── accounting/            # Financial records and chart of accounts
├── reports/               # Business analytics and reporting
├── frontend/              # Templates and static assets
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JavaScript, and images
├── digital_khata/         # Main Django project settings
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## API Endpoints

All modules have REST API endpoints for integration with mobile apps or other systems:

- `/api/inventory/` - Product management
- `/api/sales/` - Invoice management
- `/api/purchases/` - Purchase management
- `/api/accounting/` - Financial records
- `/api/reports/` - Business reports

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue on GitHub or contact the maintainers.

## Acknowledgments

- Thanks to all contributors who have helped shape Digital Khata
- Inspired by the need for affordable business management tools in emerging markets