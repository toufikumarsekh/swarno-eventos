# Project Requirements

## 1. Functional Requirements

### Authentication
- Users must be able to sign in using email and password.
- Users must be able to log out.
- Unauthenticated users must be redirected to the login page for protected views.

### Company Management
- Authenticated users must be able to register a company.
- A company must have a unique slug.
- Company registration must create an OWNER membership for the registering user.
- Users must only access company dashboards where they have an active membership.

### Clients
- Users must be able to manage clients within their company.
- Client records must be scoped to the relevant company.

### Enquiries
- Users must be able to manage enquiries within their company.
- Enquiries support client association, event information, budget and status tracking.
- Follow-ups can be scheduled for enquiries.

### Events
- Users must be able to create, list, view and edit events.
- Event-related client and enquiry selections must respect company boundaries.

### Quotations
- Users must be able to create and manage quotations.
- Quotations support multiple line items.
- Calculations include quantities, prices, discounts, taxes and totals.
- Quotations support status tracking.

### Finance
- Users must be able to record and view payments and expenses.
- Payments can be associated with relevant business records.
- Finance summaries include income, expenses and outstanding quotation calculations.
- Transactions can be voided with a recorded reason rather than silently removed.

## 2. Non-functional Requirements

- The application should use modular Django apps.
- Database credentials and secret keys must be stored outside source code.
- Company-specific data access must be enforced server-side.
- Passwords must be stored using Django's password hashing.
- Production traffic must use HTTPS.
- Static assets should be served efficiently.
- Database backups are required before production use.

## 3. Current Technical Requirements

- Python
- Django 5.2.19
- Django REST Framework 3.18.3
- PostgreSQL for persistent deployment
- SQLite for temporary demo use
- Gunicorn
- WhiteNoise

## 4. Deployment Requirement

The current public deployment is a demonstration environment. It is not approved for permanent business records because its SQLite database is on ephemeral storage.

## 5. Future Requirements

- Vendor and inventory workflows
- Workforce management
- Document storage
- Notifications
- Reporting and analytics
- Audit logging
- SaaS subscriptions and billing
