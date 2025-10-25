from channels.generic.websocket import AsyncWebsocketConsumer
import json



class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'test'
        await self.accept()
        print('Channel Connected')
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        group_data = {
            'type':'user_join',
            'message': 'Welcome to Awatech Digital World MiniChat'
        }
        await self.channel_layer.group_send(
            self.group_name,
            group_data
        )
        await self.send(text_data=json.dumps({
            'type':'welcome',
            'message':'welcome to the Group'
        }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data.get('username')
        message = data.get('message')
        group_data = {
            'type':'chat_message',
            'username': username,
            'message': message
        }
        await self.channel_layer.group_send(
            self.group_name,
            group_data
        )
        
    async def chat_message(self, event):
        username = event['username']
        message = event['message']
        text_data = {
            'type':'Response',
            'username': username,
            'message': message
        }
        await self.send(text_data=json.dumps(text_data))

    async def user_join(self, event):
        message = event['message']
        text_data = {
            'type':'user_connect',
            'message': message
        }
        await self.send(text_data=json.dumps(text_data))