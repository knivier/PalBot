# basic.py
import discord
from discord.ext import commands
import datetime

def setup_help(bot):

    @bot.command(name='commands', description="Show this help message.")
    async def commands(ctx):
        embed = discord.Embed(title="Commands Help | Prefix >", description="", color=discord.Color.blue())

        if ctx.author.guild_permissions.administrator:
            embed.add_field(name="Utilities", value=(
                ">ban | Parameters: User, Reason: Bans user from server\n"
                ">kick | Parameters: User, Reason: Kicks user from server\n"
                ">send | Parameters: User, Message: Sends a direct message to a user\n"
                ">send_embed | Parameters: @User, Title, | Message:  Sends an embedded message to a user\n"
                ">say | Parameters: Message | Makes the bot repeat a message in the current channel\n"
                ">say_embed | Parameters: Title, | Body:  Makes the bot say an embed message in the current channel\n"
            ), inline=False)

        embed.add_field(name="Fun", value=(
            ">randnum | Parameters: x, y | Generates a random number between x and y\n"
            ">flipcoin | Parameters: None | Flips a coin and shows heads or tails\n"
            ">joke | Parameters: None | Tells a random joke\n"
            ">8ball | Parameters: Question | Ask the magic 8-ball a question\n"
        ), inline=False)

        await ctx.send(embed=embed)

# This function should be called in main.py to register the commands
