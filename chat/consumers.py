from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async

from .models import Chats
import json




from asgiref.sync import async_to_sync

class  ChatConsumer(WebsocketConsumer):
    def connect(self):
        if self.scope['user'].is_anonymous:
            self.close()
        else:
            self.user=self.scope['user']
            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
            self.room_group_name = "chat_%s" % self.room_name

            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name, self.channel_name
            )

            self.accept()

    def disconnect(self, close_code):
         async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name, self.channel_name
            )





    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if "message" in text_data_json:
            message = text_data_json["message"]
            print(message)

            # Save message to database
            async_to_sync(self.create_chat)(message, self.user)
           
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "chat_message", "message": message}
            )
        else:
            print("No message found in the JSON data")

    



     # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def create_chat(self,message, user):
                return Chats.objects.create(owner=user, text=message)








# // Replace with your WebSocket URL
# var ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/my_room/');

# // Handle incoming messages
# ws.onmessage = function(event) {
#     console.log('Received message:', event.data);
# };

# // Handle errors
# ws.onerror = function(event) {
#     console.log('Error occurred:', event);
# };

# // Handle connection close
# ws.onclose = function(event) {
#     console.log('Connection closed:', event);
# };

# // Function to send a message to the server
# function sendMessage(message) {
#     if (ws.readyState === WebSocket.OPEN) {
#         ws.send(JSON.stringify({
#             'type': 'auth',
#             'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyOTM1NzgyLCJpYXQiOjE3MjI5MzM5ODIsImp0aSI6IjNhODIzNGVhMDQ2MDQ0N2Y4MjUxMjg4NDdmZTkzZjkwIiwidXNlcl9pZCI6MX0.rQCaKWTkk2BLuwJXA0YsGHBtkCNkwGwk8bjZXYxVXEs'
#         }));

#         // Send the actual message after authentication
#         ws.send(JSON.stringify({
#             'type': 'chat.message',
#             'message': message
#         }));
#     } else {
#         console.log('Connection not established yet. Trying again in 1 second.');
#         setTimeout(function() {
#             sendMessage(message);
#         }, 1000);
#     }
# }

# // Call the function to send a message
# sendMessage('Hello, server!');