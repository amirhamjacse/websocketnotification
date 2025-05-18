from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('notifications', self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'You are connected!'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('notifications', self.channel_name)

    async def send_notification(self, event):
        from .models import Notification  # lazy import here
        message = event['message']

        # Save to database asynchronously
        await sync_to_async(Notification.objects.create)(message=message)

        await self.send(text_data=json.dumps({
            'message': message
        }))
