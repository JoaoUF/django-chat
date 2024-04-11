from utils.model import Model
from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class ChatRoom(ActivatorModel, TimeStampedModel, Model):
    name = models.CharField(
        max_length=100,
        db_column='name',
    )
    slug = models.SlugField(
        unique=True,
        db_column='slug',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MAE_CHAT_ROOM'
