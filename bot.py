import discord
from discord.ext import commands
from pathlib import Path

token = Path('token.txt').read_text()
token = token.replace('\n', '')

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    print('bot is ready as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        print('Received message from {0.author}: "{0.content}"'.format(message))

client.run(token)