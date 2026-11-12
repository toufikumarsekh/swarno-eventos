# API Documentation

## 1. Overview

The backend uses Django REST Framework.

The currently confirmed API endpoint is the public health check.

The application's primary business workflows currently use Django views and templates.

## 2. Base URL

Local:

`http://127.0.0.1:8000`

Hosted demo:

`https://swarno-eventos-live.onrender.com`

## 3. Health Check

### GET `/api/health/`

Purpose: Check whether the application API is responding.

Authentication: Public (`AllowAny`).

Successful response:

```json
{
  "status": "success",
  "message": "Swarno EventOS API is running",
  "application": "Swarno EventOS",
  "version": "0.1.0"
}
```

## 4. Authentication and Permissions

The REST framework default permission class is:

`rest_framework.permissions.IsAuthenticated`

Individual API views can override this default. The health endpoint explicitly allows unauthenticated access.

## 5. Frontend Routes

The main browser routes are:

| Route | Purpose |
|---|---|
| `/` | Homepage |
| `/admin/` | Django administration |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/companies/` | Company list |
| `/companies/register/` | Company registration |
| `/companies/<slug>/dashboard/` | Company dashboard |

Company-scoped modules are mounted below:

- `/companies/<company_slug>/clients/`
- `/companies/<company_slug>/enquiries/`
- `/companies/<company_slug>/events/`
- `/companies/<company_slug>/quotations/`
- `/companies/<company_slug>/finance/`

These are frontend routes, not documented REST API endpoints.

## 6. Future API Work

Dedicated REST endpoints for clients, enquiries, events, quotations, finance and company administration have not been documented here. Add endpoint specifications only after the corresponding API views and serializers are implemented.
