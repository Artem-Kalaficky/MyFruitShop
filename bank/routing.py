from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/my-fruit-shop/bank/$", consumers.BankConsumer.as_asgi()),
]
