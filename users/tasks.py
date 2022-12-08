import datetime

import channels.layers
import httpx
import translators as ts # noqa
from asgiref.sync import async_to_sync # noqa

from my_fruit_shop.celery import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(90, task_jester.s(), name='generate_joke')


@app.task
def task_jester():
    from django.contrib.auth.models import User
    from users.models import Message

    channel_layer = channels.layers.get_channel_layer()
    jester = User.objects.get(username='jester')

    response = httpx.get('https://v2.jokeapi.dev/joke/Any?type=single')
    joke = response.json().get('joke')
    translated_joke = ts.bing(joke, from_language='en', to_language='ru')

    joke_message = Message.objects.create(user=jester, text=translated_joke, date=datetime.datetime.now())

    async_to_sync(channel_layer.group_send)(
        'shop_chat',
        {
            "type": "chat.message",
            "username": jester.first_name,
            "message": joke_message.text,
            "date": joke_message.date.strftime('%H:%M')
        }
    )
    return translated_joke
