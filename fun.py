# fun.py
import discord
from discord.ext import commands
import random

def setup_fun(bot):

    @bot.command(name='randnum', description="Generate a random number between x and y.")
    async def randnum(ctx, x: int=None, y: int=None):
        if x is None or y is None:
            await ctx.send("Please provide two numbers x and y.")
            return
        if x >= y:
            await ctx.send("Please ensure x < y for generating a range.")
            return
        number = random.randint(x, y)
        await ctx.send(f'Random number between {x} and {y}: {number}')

    @bot.command(name='flipcoin', description="Flip a coin.")
    async def flipcoin(ctx):
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(f'Coin flip result: {result}')

# This function should be called in main.py to register the commands
