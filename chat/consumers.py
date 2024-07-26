# (link unavailable)
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the connection
        await self.accept()

    async def disconnect(self, close_code):
    # Leave the chat room
        await self.channel_layer.group_discard('chat_room', self.channel_name)

        # Notify other clients in the chat room that this client has left
        # await self.channel_layer.group_send(
        #     'chat_room',
        #     {
        #         'type': 'chat.left',
        #         'username': self.username,
        #     }
        # )

    async def receive(self, text_data):
        # Handle incoming message from client
        message = text_data['message']
        user = self.scope['user']

        # Save message to database (async)
        await self.save_message(user, message)

        # Broadcast message to all connected users (async)
        await self.channel_layer.group_send(
            'chat_room',  # group name
            {
                'type': 'chat.message',
                'message': message,
                'username': user.username,
            }
        )

    async def chat_message(self, event):
        # Send message to client
        await self.send(text_data=event['message'])



# to save messages to database since orm is synchronous 
    @database_sync_to_async
    def save_message(self, user, message):
        # Save message to database (sync)
        from .models import Message
        Message.objects.create(user=user, message=message)


# returns the current user and scope has details about user like usermame,email and phonenumber
    @sync_to_async
    def get_user(self):
        # Get user instance (sync)
        return self.scope['user']