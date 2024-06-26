from rest_framework import serializers
from apps.chatapp.models import ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
