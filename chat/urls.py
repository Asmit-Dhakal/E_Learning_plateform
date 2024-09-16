# urls.py

from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumer.ChatConsumer.as_asgi()),
]
