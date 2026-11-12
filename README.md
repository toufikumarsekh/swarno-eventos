# Swarno EventOS

Swarno EventOS is a modular, multi-company event-management ERP and SaaS-ready platform built with Django.

## Live Demo

https://swarno-eventos-live.onrender.com

The demo is hosted on Render Free. Its SQLite database uses ephemeral storage, so demo records are not guaranteed to survive restarts or redeployments. Do not use this deployment for permanent business data.

## Technology Stack

- Python 3.14 (local development environment)
- Django 5.2.19
- Django REST Framework 3.18.3
- PostgreSQL support
- SQLite support for temporary demos
- HTML, CSS and JavaScript
- Django Templates
- Gunicorn
- WhiteNoise
- Render deployment

## Implemented Modules

- Email-based authentication
- Multi-company management
- Company memberships and roles
- Client management
- Enquiry management and follow-ups
- Event management
- Quotation management and calculations
- Finance dashboard
- Payments and expenses

## Planned Modules

- Vendor management
- Inventory management
- Workforce management
- Documents and notifications
- Reports and analytics
- Audit logs

See [Development Roadmap](docs/DEVELOPMENT_ROADMAP.md).

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/toufikumarsekh/swarno-eventos.git
cd swarno-eventos
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure your local Django secret key and database credentials.

The default local configuration uses PostgreSQL. Make sure the database and database user exist before running migrations.

### 5. Run migrations

```bash
cd backend
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

The custom user model uses email as its login identifier.

### 7. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Deployment

The application is deployed using Render.

- Build command: `./build.sh`
- Start command: `gunicorn --chdir backend config.wsgi:application`
- Static files: collected with Django and served through WhiteNoise.
- Database: SQLite for the current temporary demo deployment.

See [Deployment and Architecture](docs/SYSTEM_ARCHITECTURE.md).

## Repository Structure

See [Folder Structure](docs/FOLDER_STRUCTURE.txt).

## Project Status

Active development. The current deployment is intended for demonstration and testing, not production business operations.
