from django.core.management import BaseCommand

from bank.models import Bank
from my_fruit_shop import settings


class Command(BaseCommand):
    help = 'Create bank'

    def handle(self, *args, **kwargs):
        if not settings.DEBUG and not Bank.objects.all().exists():
            Bank.objects.create(amount=2000)
            self.stdout.write("Bank successfully created")
        else:
            self.stdout.write("Bank already created")
