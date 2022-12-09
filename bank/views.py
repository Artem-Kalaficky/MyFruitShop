import channels.layers
from asgiref.sync import async_to_sync # noqa
from django.http import JsonResponse

from bank.models import Bank


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
