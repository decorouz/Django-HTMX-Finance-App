import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from tracker.models import Category, Transaction, User


class Command(BaseCommand):
    help = "Generate transactions for testing"

    def handle(self, *args, **options):
        fake = Faker()

        # create categories
        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation",
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)

        user = User.objects.filter(username="agdev").first()
        if not user:
            user = User.objects.create_superuser(username="agdev", password="test")

        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 2500),
                date=fake.date_between(start_date="-1y", end_date="today"),
                type=random.choice(types),
            )
