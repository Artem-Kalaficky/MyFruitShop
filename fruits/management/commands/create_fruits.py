from django.core.management import BaseCommand

from fruits.models import Fruit
from my_fruit_shop import settings


class Command(BaseCommand):
    help = 'Create fruits'

    def handle(self, *args, **kwargs):
        if not settings.DEBUG and not Fruit.objects.all().exists():
            fruits = ['Ананас', 'Яблоко', 'Банан', 'Апельсин', 'Абрикос', 'Киви']
            for fruit in fruits:
                Fruit.objects.create(name=fruit, amount=100)
            self.stdout.write("Fruits successfully created")
        else:
            self.stdout.write("Fruits already created")
