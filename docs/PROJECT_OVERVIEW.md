# Project Overview

## 1. Project Name

Swarno EventOS

## 2. Purpose

Swarno EventOS is an event-management ERP intended to help event-management businesses organize their operations through a centralized web application.

The first intended business user is Swarno Entertainment. The architecture is designed to support multiple independent event-management companies.

## 3. Main Objectives

- Manage multiple companies within one application.
- Provide email-based user authentication.
- Associate users with companies through memberships.
- Control company access through membership roles.
- Manage clients, enquiries and follow-ups.
- Manage events and their related information.
- Prepare quotations and calculate totals.
- Track payments and expenses.
- Provide a foundation for future operational modules.

## 4. Implemented Modules

| Module | Current functionality |
|---|---|
| Accounts | Custom email-based user model, login and logout |
| Companies | Company registration, company list, dashboard and memberships |
| Clients | Company-scoped client management |
| Enquiries | Enquiries, client association, status and follow-ups |
| Events | Event creation, listing, details and editing |
| Quotations | Quotations, line items, discounts, taxes and totals |
| Finance | Finance dashboard, payments, expenses and transaction voiding |
| Core | Homepage and API health endpoint |

## 5. User and Company Structure

A user can belong to one or more companies through the Membership model.

Each membership connects one user to one company and stores that user's role and active status.

Company data access is scoped through the authenticated user's active membership.

## 6. Technology

- Backend: Python and Django
- API framework: Django REST Framework
- Frontend: Django Templates, HTML, CSS and JavaScript
- Databases: PostgreSQL and SQLite
- Production server: Gunicorn
- Static file serving: WhiteNoise
- Hosting: Render

## 7. Current Status

The application has a working hosted demonstration.

The hosted free deployment uses SQLite and should be treated as temporary. A persistent production database and production-grade hosting configuration are required before using the application for real business operations.

## 8. Future Scope

Planned areas include vendor management, inventory, workforce, documents, notifications, reporting, analytics and audit logging.
