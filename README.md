# ERP System

A comprehensive Enterprise Resource Planning (ERP) system built with Django.

## Features

- Admin Authentication & Dashboard
- Inventory Management
- Sales Tracking
- Invoicing System
- Customer Management
- Lending Module
- Email Reminders

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/erp_db
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `core/` - Main application settings and configurations
- `accounts/` - User authentication and management
- `inventory/` - Product and stock management
- `sales/` - Sales tracking and reporting
- `customers/` - Customer management
- `lending/` - Lending module
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 