import os
from dotenv import load_dotenv
from twitchio.ext import commands
from twitchio import *
load_dotenv()

TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')

class Bot(commands.Bot):
    def __init__(self):
        # Connects to Twitch
        super().__init__(token=TWITCH_TOKEN, prefix='', initial_channels=[TWITCH_CHANNEL])
        self.custom_commands = {}

    async def event_ready(self):
        # Lets us know that it's signed in and into what account!
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print(f'Joined | {TWITCH_CHANNEL}')

    async def event_message(self, message):

        msg = message.content.lower()
        if msg in self.custom_commands:
            self.custom_commands[msg](msg)
        

    def add_custom_command(self, name, func):
        self.custom_commands[name] = func

    def get_messages(self):
        return self.messages
    
def bot():
    return Bot()

def cmd(bot_instance, name):
    def decorator(func):
        bot_instance.add_custom_command(name, func)
        return func
    return decorator