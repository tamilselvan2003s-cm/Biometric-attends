"""Management command to ensure the default Super Admin account exists."""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Create the initial SUPER_ADMIN account if it does not already exist."""

    help = "Create the default Super Admin user if missing."

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

        user = User.objects.filter(username=username).first()
        if user is not None:
            self.stdout.write(
                self.style.SUCCESS(f"Super Admin '{username}' already exists (role={user.role}).")
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role="SUPER_ADMIN",
            is_approved=True,
        )
        self.stdout.write(
            self.style.SUCCESS(f"Created Super Admin '{username}' (role=SUPER_ADMIN).")
        )
