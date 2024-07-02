# main.py
import os
import discord
from discord.ext import commands
from utility import setup_moderation
from fun import setup_fun
from basic import setup_help

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

setup_moderation(bot)
setup_fun(bot)
setup_help(bot)

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the environment variables.")
    bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
    else:
        raise e
