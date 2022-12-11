from django.urls import re_path

from .consumers import BankConsumer, AuditConsumer, DeclarationConsumer

websocket_urlpatterns = [
    re_path(r"ws/my-fruit-shop/declaration/$", DeclarationConsumer.as_asgi()),
    re_path(r"ws/my-fruit-shop/bank/$", BankConsumer.as_asgi()),
    re_path(r"ws/my-fruit-shop/(?P<room_name>\w+)/$", AuditConsumer.as_asgi()),
]
