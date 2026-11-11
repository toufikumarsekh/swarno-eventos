# Swarno EventOS

A modular event-management ERP and SaaS-ready platform built with Django.

## Technology Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- HTML, CSS and JavaScript
- Django Templates

## Implemented Modules
- Authentication
- Company management
- Client management
- Enquiries
- Events
- Quotations
- Payments and expenses
- Finance dashboard
- Theme switching

## Planned Modules
- Vendor management
- Inventory management
- Workforce management
- Documents and notifications
- Reports and analytics
- Audit logs

## Local Development

Create a virtual environment and install dependencies:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Configure your local environment using `.env.example`, then:

    cd backend
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Open http://127.0.0.1:8000/

## Status
Active development.
