# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chat import urls  # Adjust this import according to your project structure

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shikshya.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                urls.websocket_urlpatterns
            )
        )
    ),
})
