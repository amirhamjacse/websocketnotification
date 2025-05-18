# chat/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Item
import json

@receiver(post_save, sender=Item)
def notify_new_item(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered for new item:", instance.name) 
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifications',  # group name
            {
                'type': 'send_notification',
                'message': f'New item created: {instance.name}'
            }
        )

