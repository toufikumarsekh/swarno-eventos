
# Changelog

## 2026-11-11 — Initial Foundation Completed

### Added
- Initial project directory structure.
- Django 5.2.19 and Django REST Framework 3.18.3.
- Python 3.14 virtual environment.
- PostgreSQL database and application user.
- Environment variable configuration.
- Django project settings and URL configuration.
- Initial database migrations.
- Django superuser.
- Core application and API health endpoint.
- Initial HTML homepage and responsive CSS.
- Local development server.

### Verified
- PostgreSQL connection successful.
- Django system check successful.
- Initial migrations successful.
- Homepage successfully opened in browser.

### Pending
- API browser verification.
- Custom user model.
- Company registration.
- Authentication and permissions.
- Multi-tenant data isolation.

## [0.1.0] - 2026-11-11

### Added
- Custom email-based authentication.
- Login and logout pages.
- Company registration workflow.
- Company and Membership database models.
- Automatic company slug generation.
- Automatic Owner membership on company registration.
- My Companies frontend page.
- Company-specific dashboard.
- Company switching functionality.
- Authenticated frontend navigation.
- Login redirect to My Companies.
- Company dashboard authorization through active membership.
- Initial responsive styling for company management pages.

### Verified
- User login and logout.
- Company creation.
- Owner membership creation.
- My Companies page.
- Company dashboard access.
- Company-specific dashboard URLs.

### Next
- Clients and Enquiries CRM module.

## [0.2.0] - 2026-11-11

### Added
- Clients CRM module with company-scoped listing, search, creation, details and editing.
- Enquiries CRM module with client association, event information, budget, status tracking and filtering.
- Follow-up scheduling for enquiries.
- Company dashboard links to Clients and Enquiries.
- Company-scoped CRM URL routing and membership checks.

### Fixed
- CRM URL namespace resolution for nested company routes.

### Verified
- Django system check passed.
- Clients and Enquiries URL reverse tests passed.
- Browser access to both CRM modules confirmed by the user.

### Next
- Complete CRM workflow testing.
- Begin Events Management module.

## [0.3.0] - 2026-11-11

### Added — Events Management

- Added and registered the Events Django app.
- Added Event model and database migration.
- Added company-scoped event creation, listing, search and status filtering.
- Added event detail and edit functionality.
- Added client and enquiry selection restricted to the current company.
- Added event form validation for enquiry/client consistency and event time.
- Added Events templates, navigation and admin registration.
- Verified event creation, detail viewing and editing.

### Next

- Begin the Quotations module.

## [0.4.0] - 2026-11-11

### Added — Quotations Management

- Added and registered the Quotations Django app.
- Added Quotation and QuotationItem models and database migration.
- Added company-scoped quotation creation, listing, search and filtering.
- Added quotation detail and draft editing functionality.
- Added multiple quotation line items with quantity, price, discount and tax.
- Added automatic subtotal, discount, tax and grand-total calculations.
- Added quotation status tracking and quotation number generation.
- Added quotation templates, dashboard navigation and admin registration.
- Fixed validation of blank extra quotation-item forms.

### Verified

- Django system check passed.
- Quotation URL reverse tests passed.
- User confirmed quotation pages are working in the browser.

### Next

- Begin Finance module.

## [0.5.0] - 2026-11-11

### Added — Finance Management

- Added and registered the Finance Django app.
- Added Payment and Expense models and database migration.
- Added automatic receipt and expense number generation.
- Added company-scoped payment and expense creation and listing.
- Added payment association with clients, events and quotations.
- Added expense categories, payment methods and transaction references.
- Added Finance dashboard with income, expenses, net cash and outstanding quotation calculations.
- Added payment and expense detail pages.
- Added transaction voiding with mandatory reasons while preserving records.
- Added Finance templates, dashboard navigation and admin registration.

### Verified

- Django system check and Finance URL reverse tests passed.
- All five main Finance pages returned HTTP 200.
- Payment and expense creation, detail and void workflows passed.
- Temporary transactions were rolled back; existing records remained unchanged.

### Next

- Begin Vendor Management.


## [0.6.0] - 2026-11-11

### Added
- Global Light/Dark theme toggle in the shared application header.
- Persistent theme preference using browser localStorage.
- Automatic restoration of the previously selected theme.
- Early theme initialization to reduce theme flashing during page loading.
- Dark theme styling for common cards, tables, forms, dashboard sections, finance sections and quotation sections.

### Changed
- Added CSS custom properties for theme-dependent colors.
- Updated the shared base template with the theme control.
- Preserved existing application routes, backend functionality and database structure.

### Verification
- Django system check and browser verification are pending confirmation.

### Next
- Complete visual verification and improve individual page layouts.
- Vendor Management remains paused during UI improvements.

## [0.7.0] - 2026-11-12

### Added — Demo Deployment

- Added SQLite selection through the `USE_SQLITE` environment variable.
- Retained PostgreSQL configuration through `DATABASE_URL` or individual database environment variables.
- Added Render deployment using Gunicorn.
- Added WhiteNoise static file serving.
- Added a build script to install dependencies, collect static files and apply migrations.
- Added `create_demo_account` management command.
- Added optional demo administrator provisioning using environment variables.
- Added automatic demo company setup and OWNER membership creation when configured.
- Deployed the application at https://swarno-eventos-live.onrender.com.

### Verified

- Render build completed successfully.
- Database migrations completed successfully.
- Gunicorn started successfully.
- Hosted homepage and login page responded successfully.
- Demo administrator login and company access were confirmed by the user.

### Deployment Notes

- The current Render Free deployment uses SQLite without a persistent disk.
- Demo data is not guaranteed to survive restarts or redeployments.
- Persistent PostgreSQL is required before production business use.

### Documentation

- Updated README and project overview.
- Added architecture, requirements, decisions, database, API, roles and roadmap documentation.
- Updated repository folder structure.
