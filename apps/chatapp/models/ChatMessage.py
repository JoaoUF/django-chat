from utils.model import Model
from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django.contrib.auth.models import User
from .ChatRoom import ChatRoom


class ChatMessage(ActivatorModel, TimeStampedModel, Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user'
    )
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        db_column='room',
    )
    messageContent = models.TextField(
        db_column='message_content',
    )

    class Meta:
        db_table = 'MAE_CHAT_MESSAGE'
        ordering = ('created',)
