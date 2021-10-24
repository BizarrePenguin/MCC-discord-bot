import discord
from discord.ext import commands
from typing import Union
from pathlib import Path

# Get root discord-bot project folder
DIR = Path(__file__).parent

# Get bot oken from file
token_path = DIR / 'token.txt'
token = token_path.read_text()
token = token.replace('\n', '')

# Define checks
def is_dm(ctx: Union[discord.Message, commands.Context]):
    return (ctx.channel.type == discord.ChannelType.private)

# Define command prefix
def command_prefix(bot, message):
    if is_dm(message):
        return ''
    else:
        return '$'

# Get commands-bot instance
bot = commands.Bot(command_prefix=command_prefix)

# Set global checks
@bot.check(is_dm)

# Set bot events
@bot.event
async def on_ready():
    print('bot is ready as {0.user}'.format(bot))

# Set bot commands
@bot.command()
async def test(ctx):
    await ctx.send('Hello there. You found the test command 👌🏼')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there! I am currently a baby bot. Please do not expect good answers from me yet.')

# Run bot
bot.run(token)