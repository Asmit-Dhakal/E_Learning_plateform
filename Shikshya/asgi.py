import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.urls import websocket_urlpatterns
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Loading settings module")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shikshya.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
