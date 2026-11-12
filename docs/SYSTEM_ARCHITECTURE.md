# System Architecture

## 1. Architecture Overview

Swarno EventOS uses a Django application with modular Django apps.

The browser communicates with Django views. Views use Django models and the configured database, then render HTML templates or return API responses.

## 2. Main Components

### Application

- Django project configuration: `backend/config/`
- Django applications: `backend/apps/`
- Templates: `backend/templates/`
- Static assets: `backend/static/`

### Installed Applications

- `apps.core`
- `apps.accounts`
- `apps.companies`
- `apps.clients`
- `apps.enquiries`
- `apps.events`
- `apps.quotations`
- `apps.finance`

### Database

The settings support three configuration paths:

1. `USE_SQLITE=True`: uses `backend/db.sqlite3`.
2. `DATABASE_URL`: configures the database using `dj-database-url`.
3. PostgreSQL environment variables: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` and `DB_PORT`.

The current hosted demo selects SQLite.

### Static Files

Django collects static assets into `backend/staticfiles`.

WhiteNoise serves collected static files through the Django deployment.

## 3. Authentication

The project uses a custom user model:

`AUTH_USER_MODEL = "accounts.User"`

The user model extends Django's `AbstractUser`, removes the username field and uses a unique email address as `USERNAME_FIELD`.

The login page uses Django's built-in `LoginView`.

## 4. Multi-company Access

The Company model represents a business.

The Membership model connects users to companies and assigns a company-level role.

Company pages and operational modules use authenticated views and membership-based access checks.

## 5. Request Flow

1. A visitor opens the application.
2. An unauthenticated visitor can access the homepage and login page.
3. The user signs in using email and password.
4. The application redirects the authenticated user to the company list.
5. The user selects a company.
6. The application checks the user's active membership.
7. The relevant company dashboard and modules are displayed.

## 6. Render Deployment

Repository: `toufikumarsekh/swarno-eventos`

Branch: `main`

Service: `swarno-eventos-live`

Public URL: https://swarno-eventos-live.onrender.com

Build command:

`./build.sh`

Start command:

`gunicorn --chdir backend config.wsgi:application`

The build script:

1. Installs requirements.
2. Collects static files.
3. Applies database migrations.
4. Runs the optional demo account setup command.

## 7. Deployment Limitations

The current Render Free demo uses SQLite on an ephemeral filesystem.

There is no persistent disk attached to this service. Database files and uploaded files must not be treated as durable across service restarts or redeployments.

The free service may spin down when inactive. It is intended for demonstrations, not continuous production use.

## 8. Production Recommendations

Before production use:

- Configure a persistent managed PostgreSQL database.
- Use secure environment variables for all credentials.
- Configure backups and recovery procedures.
- Review allowed hosts, CSRF origins and HTTPS settings.
- Configure persistent media storage if file uploads are introduced.
- Review logging, monitoring and access controls.
