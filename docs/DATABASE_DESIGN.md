# Database Design

## 1. Overview

Swarno EventOS uses Django ORM models and migrations.

The project supports PostgreSQL and SQLite through its Django database configuration.

## 2. Current Business Models

| Application | Models / responsibilities |
|---|---|
| Accounts | Custom User model |
| Companies | Company and Membership |
| Clients | Client records |
| Enquiries | Enquiry and follow-up records |
| Events | Event records |
| Quotations | Quotation and quotation line items |
| Finance | Payment and Expense |
| Core | Homepage and health endpoint; no business model documented here |

Django's built-in authentication, admin, contenttypes and session applications also create database tables.

## 3. User Model

The configured user model is:

`accounts.User`

It extends Django's `AbstractUser`, removes the username field and uses a unique email address as the login identifier.

## 4. Company Relationships

- A Company can have multiple Membership records.
- A User can have multiple Membership records.
- Each Membership belongs to one Company and one User.
- A unique database constraint applies to the Company/User pair.
- Membership stores the company-level role and active status.
- Company records can store the user who created them.

## 5. Company Data Isolation

Business views use company context and membership checks to restrict access.

All new business models and queries must preserve company-level data isolation. Cross-company access must be covered by automated tests.

## 6. Database Configuration

### SQLite

Enabled with:

`USE_SQLITE=True`

Database file:

`backend/db.sqlite3`

### PostgreSQL using DATABASE_URL

When `DATABASE_URL` is set and SQLite mode is not enabled, Django uses `dj-database-url`.

### PostgreSQL using individual variables

The fallback configuration uses:

- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

## 7. Migrations

Schema changes are managed through Django migrations.

Typical local commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

## 8. Demo Database Warning

The current Render Free service uses SQLite without a persistent disk.

The database file is on ephemeral storage. Data must not be assumed to survive a restart or redeployment.

Use persistent PostgreSQL and a backup strategy before storing real business data.

## 9. Detailed Schema Maintenance

When models change, update this document with verified field names, field types, relationships, constraints and indexes. Do not use this overview as a substitute for the Django model definitions and migrations.
