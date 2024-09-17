from django.urls import path, re_path
from .views import ChatRoomListCreate, MessageListCreate
from . import consumers

# HTTP API routes
urlpatterns = [
    path('rooms/', ChatRoomListCreate.as_view(), name='chatroom-list-create'),
    path('rooms/<str:room_name>/messages/', MessageListCreate.as_view(), name='message-list-create'),
]

# WebSocket routes
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
