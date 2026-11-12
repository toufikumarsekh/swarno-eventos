import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db import transaction

from apps.companies.models import Company, Membership


class Command(BaseCommand):
    help = "Create or update the demo administrator and company."

    @transaction.atomic
    def handle(self, *args, **options):
        email = os.getenv("DEMO_ADMIN_EMAIL")
        password = os.getenv("DEMO_ADMIN_PASSWORD")
        company_name = os.getenv(
            "DEMO_COMPANY_NAME", "Swarno Entertainment"
        )

        if not email or not password:
            self.stdout.write("Demo account variables not set; skipping.")
            return

        User = get_user_model()

        user, created = User.objects.get_or_create(email=email)

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        company, _ = Company.objects.get_or_create(
            name=company_name,
            defaults={"created_by": user},
        )

        Membership.objects.get_or_create(
            company=company,
            user=user,
            defaults={"role": Membership.Role.OWNER},
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Demo administrator ready: {email}"
            )
        )
