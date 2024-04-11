from django.urls import path
from apps.chatapp.consumers import ChatRoomConsumer

websocket_urlpatterns = [
    path('ws/<str:room_name>/', ChatRoomConsumer.as_asgi())
]
