# Generated by Django 3.2 on 2022-12-10 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221208_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 18, 16, 39, 79086), verbose_name='Дата'),
        ),
    ]