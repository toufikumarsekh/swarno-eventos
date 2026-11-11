
# SWARNO EVENTOS — MASTER PROJECT CONTEXT

## 1. Project Identity

Project Name: Swarno EventOS
Original Business: Swarno Entertainment
Product Type: Event Management ERP and SaaS Platform
Initial Deployment: Local Development
Initial Market: India
Currency: INR
Language: English

Purpose:
Build a complete event management platform that helps event
organisers manage their businesses, clients, events, finances,
vendors, equipment and employees from one application.

The software will initially be used by Swarno Entertainment
and later offered to multiple event management companies.

## 2. Final Technology Stack

Operating System: Ubuntu Linux

Backend:
- Python
- Django
- Django REST Framework

Frontend:
- HTML
- CSS
- JavaScript
- Django Templates

Database:
- PostgreSQL

Development:
- Local development first
- Git for version control
- Python virtual environment

Architecture:
- Modular Monolith
- Multi-tenant SaaS-ready design

Frontend Framework:
- No React
- No Angular
- No Vue

## 3. Main Business Modules

1. User Authentication
2. Company Management
3. Client Management (CRM)
4. Enquiry Management
5. Event Management
6. Quotation Management
7. Finance and Payments
8. Vendor Management
9. Inventory and Equipment
10. Workforce Management
11. Document Management
12. Notifications
13. Reports and Analytics
14. Audit Logs

## 4. User Roles

- Platform Super Admin
- Company Owner
- Company Admin
- Event Manager
- Accountant
- Inventory Manager
- HR / Staff Manager
- Event Staff
- Client

Users must only access features and company data
permitted by their roles.

## 5. Multi-Tenant Architecture

The platform must support multiple event management companies.

Each company must have isolated business data.

Main approach:
- Shared PostgreSQL database.
- Company-wise data separation.
- company_id on tenant-owned records or equivalent
  tenant-scoped relationships.
- Server-side permission checks.
- Cross-company access must be prevented.

## 6. Financial Rules

- Use PostgreSQL NUMERIC fields for monetary values.
- Do not use floating-point values for money.
- Client advances must not automatically count as revenue.
- Track vendor bills and vendor payments separately.
- Preserve quotation versions.
- Do not delete posted financial transactions.
- Use reversal or void operations.
- Maintain financial audit history.

## 7. Inventory Rules

- Track company-owned and rented equipment separately.
- Track equipment availability.
- Prevent allocation beyond available quantity.
- Consider overlapping event dates.
- Maintain inventory movement history.

## 8. Backend Architecture

Backend location:
backend/

Django project:
backend/config/

Django applications:
backend/apps/

Applications:
- accounts
- companies
- core
- clients
- enquiries
- events
- quotations
- finance
- vendors
- inventory
- workforce
- documents
- notifications
- reports
- audit

Each application should contain suitable:
- models.py
- views.py
- serializers.py
- urls.py
- services.py
- admin.py
- tests.py

Create additional modules only when required.

## 9. Frontend Architecture

Frontend location:
frontend/

Django templates:
backend/templates/

Static assets:
backend/static/

Technologies:
- HTML
- CSS
- JavaScript

The interface must be:
- Responsive
- Mobile-friendly
- Desktop-friendly
- Easy to use
- Professional
- Consistent across modules

## 10. Database

Database: PostgreSQL

Initial database name:
swarno_eventos

Initial database user:
swarno_app

Database configuration must be stored in environment
variables, not hardcoded in application code.

Never store actual passwords or secret keys in this file.

## 11. Security Requirements

- Secure authentication
- Password hashing
- Role-based access control
- Company-level data isolation
- CSRF protection
- Input validation
- Secure file uploads
- Audit logging
- Cross-tenant access testing

## 12. Development Roadmap

Phase 1:
Project setup, dependencies and PostgreSQL configuration.

Phase 2:
Authentication, company registration and permissions.

Phase 3:
Client CRM and enquiry management.

Phase 4:
Event management.

Phase 5:
Quotations and quotation revisions.

Phase 6:
Finance, payments and expenses.

Phase 7:
Vendor management.

Phase 8:
Inventory and equipment allocation.

Phase 9:
Workforce management.

Phase 10:
Documents, notifications and reports.

Phase 11:
Security testing and local deployment.

## 13. Development Progress

Current Status:
Folder structure created.

Completed:
- Project root created.
- Backend folders created.
- Frontend folders created.
- Documentation folders created.
- Database folders created.
- Testing folders created.
- Git repository initialised.

Pending:
- Master project documentation completion.
- Python virtual environment.
- Django installation.
- PostgreSQL configuration.
- Django project initialisation.
- Database connection.
- Authentication implementation.

## 14. Important Development Rules

1. Explain commands in beginner-friendly language.
2. Provide complete working code.
3. Give commands in the correct execution order.
4. Do not skip database migrations.
5. Do not overwrite existing code without explaining.
6. Keep project documentation updated.
7. Update CHANGELOG.md after meaningful changes.
8. Keep secrets outside Git.
9. Test every major module.
10. Maintain multi-tenant security from the beginning.

## 15. Current Next Task

Complete project documentation.

Then begin Phase 1:
Python environment, Django installation and PostgreSQL setup.

---

# 16. IMPLEMENTATION STATUS — 11 NOVEMBER 2026

## Project Foundation

Status: COMPLETED

Project location:
~/projects/swarno-eventos

Operating system:
Ubuntu Linux

Version control:
Git repository initialised.

Initial structure:
52 directories and 43 files.

## Installed Technology

Python: 3.14.4
Virtual environment: .venv
Django: 5.2.19
Django REST Framework: 3.18.3
psycopg: 3.3.8
python-dotenv: 1.2.4
PostgreSQL: 18.6 (client version reported by psql)

## Database Configuration

Database name: swarno_eventos
Database user: swarno_app
Database host: 127.0.0.1
Database port: 5432

Database connection:
TESTED SUCCESSFULLY.

Credentials are stored in the root .env file.
Never copy actual passwords or secret keys into documentation.

## Django Configuration

Django project location:
backend/config/

Configured files:
- backend/manage.py
- backend/config/settings.py
- backend/config/urls.py
- backend/config/asgi.py
- backend/config/wsgi.py

Configured features:
- PostgreSQL connection
- Environment variable loading
- Django admin
- Django authentication framework
- Django REST Framework
- Static file configuration
- Asia/Kolkata timezone
- Default authenticated API permissions

Core application:
backend/apps/core/

Implemented core files:
- apps.py
- views.py

## Implemented Features

1. Project directory structure.
2. Python virtual environment.
3. Django installation.
4. PostgreSQL database and user.
5. Django database connection.
6. Initial Django migrations.
7. Django superuser account.
8. Homepage view.
9. Homepage HTML template.
10. Homepage CSS styling.
11. Admin URL.
12. API health-check endpoint.

Homepage:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

Health API:
http://127.0.0.1:8000/api/health/

Homepage confirmed working by user.
API endpoint implemented; independent browser verification pending.

## Current Frontend

Template:
backend/templates/base.html

Stylesheet:
backend/static/css/style.css

Frontend technology:
HTML, CSS and JavaScript.

Current homepage contains:
- Swarno EventOS branding
- System status indicator
- Welcome section
- Admin panel link
- Eight visual module placeholders
- Responsive layout

The eight modules are placeholders.
They are NOT functional business modules yet.

## Current Backend Status

Django backend is running locally.

Implemented business functionality:
- No CRM functionality yet.
- No enquiry management yet.
- No event management yet.
- No quotation management yet.
- No finance functionality yet.
- No vendor management yet.
- No inventory functionality yet.
- No workforce functionality yet.
- No multi-company registration yet.
- No role-based business permissions yet.

The corresponding application directories are currently structural placeholders.

## Security and Configuration Notes

- Root .env contains local secrets.
- .env must remain excluded from Git.
- .env.example contains placeholders.
- Django development server is for local development only.
- Multi-tenant security has not yet been implemented.
- No production deployment has been performed.

## Development Progress

Phase 0: Folder structure — COMPLETED.
Phase 1: Environment and database foundation — COMPLETED.
Phase 1: Django configuration — COMPLETED.
Phase 1: Basic homepage — COMPLETED.

Phase 2: Authentication and company management — PENDING.
Phase 3: Client CRM and enquiries — PENDING.
Phase 4: Event management — PENDING.
Phase 5: Quotations — PENDING.
Phase 6: Finance — PENDING.
Phase 7: Vendors — PENDING.
Phase 8: Inventory — PENDING.
Phase 9: Workforce — PENDING.
Phase 10: Documents, notifications and reports — PENDING.
Phase 11: Security testing and deployment — PENDING.

## Next Development Task

Begin Phase 2:

1. Design a custom user model before creating business users.
2. Implement company registration and company profiles.
3. Implement company-owner accounts.
4. Implement login and logout.
5. Implement role-based access control.
6. Establish and test company-level data isolation.
7. Build a protected dashboard.

IMPORTANT:
Design the custom user model before adding further business
models or creating additional production data.

---

# Development Progress — 11 November 2026

## Completed: Authentication and Company Management Foundation

### Backend
- Django 5.2.19 configured with PostgreSQL.
- Django REST Framework installed and configured.
- Custom email-based User model implemented.
- Login and logout functionality implemented.
- Company and Membership models implemented.
- Company ownership and role-based membership established.
- Company registration uses database transactions.
- Company slugs generated automatically and uniquely.
- Company dashboard access restricted to active company members.

### Frontend
- Base HTML template with shared layout.
- Login page.
- Company registration page.
- My Companies selection page.
- Individual company dashboard.
- Company switching links.
- Add Company navigation.
- Logout navigation.
- Responsive styling for company selection and dashboard.

### Working User Flow
1. User opens Swarno EventOS.
2. User logs in using email and password.
3. User is redirected to My Companies.
4. User selects a company.
5. User enters that company's dashboard.
6. User can register another company or switch companies.
7. User can log out.

### Important Routes
- Homepage: /
- Login: /accounts/login/
- Logout: /accounts/logout/
- My Companies: /companies/
- Register Company: /companies/register/
- Company Dashboard: /companies/<slug>/dashboard/
- Django Admin: /admin/
- API Health: /api/health/

### Current Development Environment
- Python 3.14.4
- Django 5.2.19
- Django REST Framework 3.18.3
- PostgreSQL 18.6
- psycopg 3.3.8
- Ubuntu Linux
- Local development server

### Verified Functionality
- Login successfully redirects to My Companies.
- Company registration successfully creates a company.
- Company registration automatically creates an Owner membership.
- Company dashboard loads successfully.
- Company-specific dashboard access works.
- Logout successfully returns the user to the homepage.

### Example Verified Company Workspaces
- sdfhg — /companies/sdfhg/dashboard/
- toufik-umar — /companies/toufik-umar/dashboard/

### Important Architecture Notes
- Continue using a modular Django monolith.
- Keep company data isolated by company membership.
- Never rely only on frontend checks for authorization.
- Every company-specific business record must be associated with its company.
- Do not expose one company's records to another company.
- Do not store plaintext passwords or secrets in project documentation.

### Next Development Phase
Build the CRM foundation:

1. Client management.
2. Enquiry management.
3. Enquiry follow-up tracking.
4. Convert an enquiry into an event.
5. Company-scoped access and permissions.

After CRM, continue with Event Management, Quotations, Finance, Vendors, Inventory, Workforce, Documents, Notifications and Reports.

## Development Progress — 11 November 2026 (CRM)

### Clients Module
- Client model created with company association.
- Client details include name, email, phone, alternate phone, address, city and notes.
- Client creation and editing forms implemented.
- Company-scoped client listing and search implemented.
- Client detail page implemented.
- Client records are associated with their creator.

### Enquiries Module
- Enquiry model created with company and client associations.
- Enquiry details include title, event type, event date, guest count, venue, budget, source, status and description.
- Enquiry statuses: New, Contacted, Qualified, Proposal, Converted and Lost.
- Enquiry creation, listing, filtering, detail and editing implemented.
- FollowUp model and follow-up scheduling form implemented.
- Company-scoped enquiry and client selection implemented.

### CRM Routing and Access
- CRM routes integrated under company-specific URLs.
- Clients namespace: companies:clients
- Enquiries namespace: companies:enquiries
- Active company membership checks implemented in CRM views.
- Dashboard links added for Clients and Enquiries.
- Django URL reverse tests passed for both CRM modules.

### Verification Status
- Django system check passed.
- Clients and Enquiries URL reverse tests passed.
- User confirmed both CRM modules are working in the browser.
- Full CRUD and follow-up workflow testing is still pending.

### Next Development Module
- Events Management: event creation, event details, event status, scheduling, venue, client association and company-level access control.

## Development Progress — 11 November 2026 (Events Module)

### Events Management — Implemented and tested

- Registered and configured the Django Events app.
- Created the Event model with company, client, enquiry, event type, date, time, venue, guest count, budget, status, description and notes.
- Added EventForm with company-scoped client and enquiry selection.
- Implemented company-scoped event listing, search, status filtering, creation, detail and editing views.
- Added Events URLs under the company dashboard.
- Added Events list, form and detail templates.
- Registered Event in Django admin.
- Added Events navigation and styling.
- Created and applied database migrations.
- Verified event listing, event creation, event details and event editing successfully.

### Current working modules

1. Accounts and authentication
2. Multi-company registration and membership
3. Company dashboard
4. Clients / CRM
5. Enquiries and follow-ups
6. Events Management

### Next module

Quotations — quotation creation, line items, pricing, discounts, taxes, versioning and quotation status management.

## Development Progress — 11 November 2026 (Quotations Module)

### Quotations Management — Implemented and browser-tested

- Registered and configured the Django Quotations app.
- Created Quotation and QuotationItem models.
- Added quotation number generation and quotation status tracking.
- Added client and optional event association with company-scoped form selection.
- Implemented quotation creation, listing, search, filtering and detail viewing.
- Added multiple line items with quantity, unit, unit price, discount and tax.
- Implemented automatic subtotal, discount, tax and grand-total calculations.
- Added draft quotation editing; non-draft quotations are currently view-only.
- Added quotation templates, company dashboard navigation and Django admin registration.
- Created and applied the initial Quotations database migration.
- Fixed blank extra-item validation to prevent errors when opening the quotation form.
- Verified Django system checks, URL resolution and browser access.

### Current working modules

1. Accounts and authentication
2. Multi-company registration and membership
3. Company dashboard
4. Clients / CRM
5. Enquiries and follow-ups
6. Events Management
7. Quotations Management

### Next Development Module

Finance — client advances, client payments, expenses, payment records and transaction tracking.

## Development Progress — 11 November 2026 (Finance Module)

### Finance Management — Implemented and tested

- Registered and configured the Django Finance app.
- Created Payment and Expense models with database migration.
- Added automatic receipt number and expense number generation.
- Added client payment types: advance, partial, final and other.
- Added payment methods, transaction references, dates and notes.
- Added expense categories, payee details and payment methods.
- Added company-scoped payment and expense creation and listing.
- Added finance dashboard with posted income, expenses, net cash and outstanding quotation amounts.
- Connected payments with clients, events and quotations.
- Added payment and expense detail pages.
- Implemented transaction voiding with mandatory reasons and preserved records.
- Added Finance Django admin registration and dashboard navigation.
- Added company membership checks and company-scoped transaction access.
- Created and applied the initial Finance database migration.

### Verification

- Django system check passed.
- Finance URL reverse tests passed.
- All five main Finance pages returned HTTP 200.
- Payment creation, detail viewing and voiding tested successfully.
- Expense creation, detail viewing and voiding tested successfully.
- Temporary test transactions were rolled back successfully.
- Existing payment and expense counts remained unchanged.

### Current working modules

1. Accounts and authentication
2. Multi-company registration and membership
3. Company dashboard
4. Clients / CRM
5. Enquiries and follow-ups
6. Events Management
7. Quotations Management
8. Finance Management

### Next Development Module

Vendor Management — vendor registration, contact details, services, quotations, bills and payment tracking.



## Development Progress — 11 November 2026 (Global Theme Switching)

### Theme Switching
Implemented a global Light/Dark theme switching feature.

**Files updated:**
- `backend/templates/base.html`
- `backend/static/css/style.css`

**Features implemented:**
- Added a theme toggle button to the shared application header.
- Theme switching is available across all pages extending `base.html`.
- Light theme is the default for first-time visitors.
- Dark theme uses CSS custom properties and the `data-theme="dark"` attribute.
- Theme selection is saved in browser `localStorage` using the key `swarno-theme`.
- Previously selected theme is restored when navigating between pages or reopening the application.
- Theme initialization runs before page rendering to reduce incorrect-theme flashes.
- Added dark-theme styling for common application components:
  - Page backgrounds and text
  - Headers and navigation
  - Cards and dashboard sections
  - Tables and table rows
  - Forms, inputs, selects and textareas
  - Finance and quotation sections
  - Error messages and feedback
  - Footer and welcome section

**Implementation details:**
- No additional JavaScript package or Django dependency required.
- Theme preference is stored locally in the user's browser.
- Existing backend models, database records, URLs and business logic remain unchanged.

**Verification status:**
- Django system check should be run after the update.
- Browser verification of both themes and persistence is pending.

**Next UI tasks:**
1. Verify Light/Dark switching across all modules.
2. Fix any individual components with poor contrast.
3. Continue improving page layouts, forms, tables and detail views.
4. Keep Vendor Management paused until the interface improvement work is complete.
