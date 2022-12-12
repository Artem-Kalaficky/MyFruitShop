from django.urls import re_path

from .consumers import FruitConsumer

websocket_urlpatterns = [
    re_path(r"ws/my-fruit-shop/fruit/$", FruitConsumer.as_asgi()),
]
