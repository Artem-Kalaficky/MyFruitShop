# Generated by Django 3.2 on 2022-12-11 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 14, 42, 44, 91981), verbose_name='Дата'),
        ),
    ]
