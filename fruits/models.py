import datetime

from django.db import models


class Status(models.TextChoices):
    SUCCESS = 'SS', 'SUCCESS'
    ERROR = 'ER', 'ERROR'


class Fruit(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фрукт'
        verbose_name_plural = 'Фрукты'
        ordering = ['name']


class Log(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE, verbose_name='Фрукт')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.SUCCESS, verbose_name='Статус')
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата')
    amount = models.IntegerField(verbose_name='Кол-во фруктов')
    usd = models.IntegerField(verbose_name='Сумма USD')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        ordering = ['date']
