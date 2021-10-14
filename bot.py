import discord
from discord.ext import commands
from pathlib import Path

token = Path.read_text('token.txt')
token = token.replace('\n', '')

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    print('bot is ready as {0.user}', client)

client.run(token)