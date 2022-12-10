from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/my-fruit-shop/bank/$", consumers.BankConsumer.as_asgi()),
    re_path(r"ws/my-fruit-shop/(?P<room_name>\w+)/$", consumers.AuditConsumer.as_asgi()),
]
