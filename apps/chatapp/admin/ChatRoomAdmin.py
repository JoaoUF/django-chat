from django.contrib import admin
from apps.chatapp.models import ChatRoom


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    pass
