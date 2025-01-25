import aiohttp
from datetime import datetime
import asyncio
import logging

logger = logging.getLogger(__name__)

class APIClient:
    async def get_messages(self):
        logger.debug("Fetching messages from API")
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, headers=self.headers) as response:
                data = await response.json()
                logger.debug(f"API Response: {data}")
                return data

    async def send_message(self, content, chat_id):
        logger.debug(f"Sending message to chat {chat_id}: {content}")

    def __init__(self, token):
        self.token = token
        self.base_url = 'http://p2pchat.whf.bz/login/Bots/api/bot_endpoint.php'
        self.headers = {'Authorization': f'Bot {token}'}
        self.session = None
        self.last_check = 0
        
    async def _get_session(self):
        if not hasattr(self, 'session'):
            self.session = aiohttp.ClientSession(headers=self.headers)
        return self.session

    async def _create_session(self):
        return aiohttp.ClientSession(headers=self.headers)


    async def _ensure_session(self):
        if self.session is None:
            self.session = aiohttp.ClientSession(headers=self.headers)
        return self.session

    async def get_bot_info(self):
        session = await self._ensure_session()
        params = {'bot_info': '1'}
        async with session.get(self.base_url, params=params) as response:
            data = await response.json()
            return data

    async def get_messages(self):
        session = await self._ensure_session()
        params = {'last_check': self.last_check}
        async with session.get(self.base_url, params=params) as response:
            data = await response.json()
            return data

    async def send_message(self, content, chat_id):
        session = await self._ensure_session()
        data = {'content': content}
        async with session.post(self.base_url, json=data) as response:
            return await response.json()

    async def get_user_data(self, username):
        session = await self._ensure_session()
        params = {'username': username}
        async with session.get(self.base_url, params=params) as response:
            data = await response.json()
            return data.get('user')

    async def start_bot_loop(self, command_handler):
        while True:
            try:
                messages = await self._get_messages()
                for message in messages.get('messages', []):
                    if message['timestamp'] > self.last_timestamp:
                        await self._handle_command(message, command_handler)
                        self.last_timestamp = message['timestamp']
            except Exception:
                pass
            await asyncio.sleep(1)

    async def _handle_command(self, message, command_handler):
        command, args = parse_command(message)
        if command:
            ctx = {
                'message': message,
                'chat_id': message.get('chat_id'),
                'args': args,
                'api': self
            }
            if command in command_handler.commands:
                await execute_command(command_handler.commands[command].callback, ctx)


    async def get_user_data(self, username):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.api_url,
                headers=self.headers,
                params={"username": username}
            ) as response:
                data = await response.json()
                return data.get('user')