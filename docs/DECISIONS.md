# Architecture and Technical Decisions

## 1. Django

**Decision:** Use Django as the main backend framework.

**Reason:** Django provides authentication, ORM, migrations, administration, templates and a modular application structure.

## 2. Modular Applications

**Decision:** Separate business features into Django apps.

**Current apps:** Core, Accounts, Companies, Clients, Enquiries, Events, Quotations and Finance.

**Reason:** Keep features organized and make future modules easier to add.

## 3. Custom Email-based User Model

**Decision:** Use `apps.accounts.User`, extending Django's `AbstractUser`.

**Reason:** Users sign in with email rather than a username.

The configured user model is `accounts.User`.

## 4. Multi-company Membership

**Decision:** Use separate Company and Membership models.

**Reason:** A user can be associated with multiple companies, with a role assigned separately for each company.

A unique constraint prevents duplicate memberships for the same company and user.

## 5. Database Support

**Decision:** Support PostgreSQL and SQLite.

- PostgreSQL is the intended database for persistent deployments.
- SQLite is available for local experiments and the temporary hosted demo.
- `DATABASE_URL` can configure a database through `dj-database-url`.

**Important:** SQLite on Render Free without a persistent disk is not suitable for permanent business records.

## 6. Static Files

**Decision:** Use WhiteNoise with Django static-file collection.

**Reason:** Serve application static files without requiring a separate static server for the current deployment.

## 7. Hosting

**Decision:** Use Render for the demonstration deployment.

**Reason:** Provide a publicly accessible demonstration without maintaining a server.

The current free service is not the production hosting decision.

## 8. Demo Administrator Provisioning

**Decision:** Provide a Django management command named `create_demo_account`.

The command reads:

- `DEMO_ADMIN_EMAIL`
- `DEMO_ADMIN_PASSWORD`
- `DEMO_COMPANY_NAME`

If email or password is missing, the command skips setup.

When configured, it creates or updates the demo administrator, ensures the demo company exists and creates an OWNER membership if one does not already exist.

The command runs after migrations in `build.sh`.

The password is supplied through environment variables, not committed to source control. Because the command resets the configured user's password whenever it runs, keep the environment variable current and private.
