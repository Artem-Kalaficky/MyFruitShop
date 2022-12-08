from django.contrib.auth.models import User
from django.core.management import BaseCommand

from my_fruit_shop import settings


class Command(BaseCommand):
    help = 'Create users'

    def handle(self, *args, **kwargs):
        if not settings.DEBUG and not User.objects.all().exists():
            users = [('admin', 'Иван'), ('jester', 'Шутник'), ('ashot', 'Ашот')]
            for user in users:
                user = User.objects.create(username=user[0], first_name=user[1], is_staff=True, is_superuser=True)
                user.set_password('Zaqwerty123')
                user.save()
            self.stdout.write("Users successfully created")
        else:
            self.stdout.write("Users already created")
