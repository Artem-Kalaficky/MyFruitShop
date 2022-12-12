import datetime
import random

import channels.layers
from asgiref.sync import async_to_sync # noqa
from django_celery_beat.models import IntervalSchedule, PeriodicTasks, PeriodicTask

from bank.models import Bank
from fruits.models import Fruit, Log, Status, Operation
from my_fruit_shop.celery import app

channel_layer = channels.layers.get_channel_layer()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5, task_buy_fruits.s(1), name='buy_ananas')
    sender.add_periodic_task(7, task_buy_fruits.s(2), name='buy_apple')
    sender.add_periodic_task(9, task_buy_fruits.s(3), name='buy_banana')
    sender.add_periodic_task(11, task_buy_fruits.s(4), name='buy_orange')
    sender.add_periodic_task(13, task_buy_fruits.s(5), name='buy_apricot')
    sender.add_periodic_task(15, task_buy_fruits.s(6), name='buy_kiwi')


@app.task
def task_buy_fruits(fruit_id, amount=None, cost_for_unit=None):
    fruit = Fruit.objects.get(pk=fruit_id)
    cost_for_unit = cost_for_unit if cost_for_unit else random.choice(range(1, 5))
    amount = amount if amount else random.choice(range(1, 21))
    bank = Bank.objects.first()
    usd = cost_for_unit * amount

    log = Log.objects.create(
        fruit=fruit,
        status=Status.ERROR if usd > bank.amount else Status.SUCCESS,
        date=datetime.datetime.now(),
        amount=amount,
        usd=usd,
        operation=Operation.BUY
    )

    async_to_sync(channel_layer.group_send)(
        'shop_fruit',
        {
            "type": "update.fruit",
            "status": log.get_status_display(),
            "fruit_id": fruit.id,
            "fruit_name": fruit.name,
            "date": log.date.strftime('%d.%m.%Y %H:%M'),
            "amount": amount,
            "usd": usd,
            "operation": log.get_operation_display()
        }
    )

    fruit.amount += amount
    bank.amount -= usd
    fruit.save()
    bank.save()

    async_to_sync(channel_layer.group_send)(
        'shop_bank',
        {
            "type": "update.bank.account",
            "amount": bank.amount
        }
    )

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=random.choice(range(5, 21)),
        period=IntervalSchedule.SECONDS,
    )
    task = PeriodicTask.objects.get(task='users.tasks.task_jester')
    task.interval = schedule
    task.save()
    PeriodicTasks.changed(task)
    return 'OK'


@app.task
def task_sell_fruits(fruit_id, amount=None, cost_for_unit=None):
    fruit = Fruit.objects.get(pk=fruit_id)
    cost_for_unit = cost_for_unit if cost_for_unit else random.choice(range(1, 5))
    amount = amount if amount else random.choice(range(1, 21))
    bank = Bank.objects.first()
    usd = cost_for_unit * amount

    log = Log.objects.create(
        fruit=fruit,
        status=Status.ERROR if amount > fruit.amount else Status.SUCCESS,
        date=datetime.datetime.now(),
        amount=amount,
        usd=usd,
        operation=Operation.SELL
    )

    async_to_sync(channel_layer.group_send)(
        'shop_fruit',
        {
            "type": "update.fruit",
            "status": log.get_status_display(),
            "fruit_id": fruit.id,
            "fruit_name": fruit.name,
            "date": log.date.strftime('%d.%m.%Y %H:%M'),
            "amount": amount,
            "usd": usd,
            "operation": log.get_operation_display()
        }
    )

    fruit.amount -= amount
    bank.amount += usd
    fruit.save()
    bank.save()

    async_to_sync(channel_layer.group_send)(
        'shop_bank',
        {
            "type": "update.bank.account",
            "amount": bank.amount
        }
    )
