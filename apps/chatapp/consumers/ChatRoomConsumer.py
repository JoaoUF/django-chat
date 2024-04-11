from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from apps.chatapp.models import ChatRoom, ChatMessage


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.room_group_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        username = data['username']
        message = data['message']
        room = data['room']

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'room': room,
                'username': username,
            }
        )

        await self.save_message(username,room,message)

    async def chat_message(self, event):
        username = event['username']
        message = event['message']
        room = event['room']

        await self.send(text_data=json.dump({
            'message': message,
            'room': room,
            'username': username,
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(name=room)

        ChatMessage.objects.create(user=user, room=room, messageContent=message)
