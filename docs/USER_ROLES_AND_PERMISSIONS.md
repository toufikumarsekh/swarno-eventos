# User Roles and Permissions

## 1. Membership Model

Company-level access is represented by the `Membership` model.

Each membership connects one user to one company and contains:

- Company
- User
- Role
- Active status
- Join timestamp

A database uniqueness constraint prevents duplicate memberships for the same company and user.

## 2. Available Roles

The following roles are defined in `apps/companies/models.py`.

| Role key | Display name |
|---|---|
| `owner` | Owner |
| `admin` | Administrator |
| `event_manager` | Event Manager |
| `accountant` | Accountant |
| `inventory_manager` | Inventory Manager |
| `hr_manager` | HR / Staff Manager |
| `staff` | Event Staff |
| `client` | Client |

## 3. Owner Membership

When a user registers a company through the company registration workflow, the application creates an OWNER membership for that user.

The hosted demo setup command also creates an OWNER membership for the configured demo administrator when the membership does not already exist.

## 4. Access Control

Company dashboards and business modules require authentication.

Company dashboard access checks for an active membership connecting the logged-in user to the requested company.

Operational views should continue to enforce company-scoped queries and permissions. Hiding navigation links alone is not an authorization mechanism.

## 5. Django Staff and Superuser Flags

Django's `is_staff` and `is_superuser` flags are separate from company membership roles.

- `is_staff` permits access to Django's admin site, subject to Django permissions.
- `is_superuser` grants Django's superuser permissions.
- A company OWNER membership grants the application-level company role.

These concepts should not be treated as interchangeable.

## 6. Future Permission Work

The role choices are defined, but detailed role-by-role permission policies still need to be implemented and tested across every business module.
