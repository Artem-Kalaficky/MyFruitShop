import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import bank.routing
import fruits.routing
import users.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_fruit_shop.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(
            fruits.routing.websocket_urlpatterns
            + users.routing.websocket_urlpatterns
            + bank.routing.websocket_urlpatterns
        ))
    ),
})
