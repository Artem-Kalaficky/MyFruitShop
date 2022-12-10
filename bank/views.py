import channels.layers
from asgiref.sync import async_to_sync # noqa
from django.core.cache import cache
from django.http import JsonResponse

from bank.models import Bank
from bank.tasks import task_check_warehouse


def update_bank_account(request):
    channel_layer = channels.layers.get_channel_layer()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'GET':
        bank = Bank.objects.first()
        if not request.GET.get('withdraw'):
            bank.amount += int(float(request.GET.get('amount')))
        else:
            bank.amount -= int(float(request.GET.get('amount')))
        bank.save()

        async_to_sync(channel_layer.group_send)(
            'shop_bank',
            {
                "type": "update.bank.account",
                "amount": bank.amount
            }
        )

        return JsonResponse({"updated_amount": bank.amount}, status=200)


def start_audit(request):
    if request.is_ajax() and request.method == 'GET':
        user_id = request.GET.get('userId')
        if cache.get(f'user_{user_id}') is None:
            cache.set(f'user_{user_id}', 1)
            task_check_warehouse.delay(user_id)
            return JsonResponse({}, status=200)
        return JsonResponse({}, status=400)
