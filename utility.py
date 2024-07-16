# utility.py
import discord
from discord.ext import commands
import datetime

def setup_moderation(bot):
    @bot.command(name='kick', description="Kick a user from the server.")
    @commands.has_permissions(administrator=True)
    async def kick(ctx, member: discord.Member=None, *, reason=None):
        if member is None or not isinstance(member, discord.Member):
            await ctx.send("Invalid user. Please mention a valid user to kick.", delete_after=10)
            return
        if reason is None:
            await ctx.send("Please provide a reason for kicking this user.", delete_after=10)
            return

        try:
            await member.send(f'You have been kicked from {ctx.guild.name} for: {reason}')
        except discord.HTTPException:
            pass  # Failed to send a DM, continue anyway

        await member.kick(reason=reason)
        await ctx.send(f'User {member.mention} has been kicked for: {reason}')

    @bot.command(name='ban', description="Ban a user from the server.")
    @commands.has_permissions(administrator=True)
    async def ban(ctx, member: discord.Member=None, *, reason=None):
        if member is None or not isinstance(member, discord.Member):
            await ctx.send("Invalid user. Please mention a valid user to ban.", delete_after=10)
            return
        if reason is None:
            await ctx.send("Please provide a reason for banning this user.", delete_after=10)
            return

        if member.guild != ctx.guild:
            await ctx.send("This user is not a member of this server.", delete_after=10)
            return

        try:
            await member.send(f'You have been banned from {ctx.guild.name} for: {reason}')
        except discord.HTTPException:
            pass  # Failed to send a DM, continue anyway

        await member.ban(reason=reason)
        await ctx.send(f'User {member.mention} has been banned for: {reason}')

    @bot.command(name='send', description="Send a direct message to a user.")
    @commands.has_permissions(administrator=True)
    async def send(ctx, member: discord.Member=None, *, msg=None):
        if member is None or not isinstance(member, discord.Member):
            await ctx.send("Invalid user. Please mention a valid user to send a message.", delete_after=10)
            return
        if msg is None:
            await ctx.send("Please provide a message to send to the user.", delete_after=10)
            return

        try:
            await member.send(f'You have received a message: {msg}')
            await ctx.send(f'Message sent to {member.mention}')
        except discord.HTTPException:
            await ctx.send(f'Failed to send message to {member.mention}', delete_after=10)

    @bot.command(name='send_embed', description="Send an embedded message to a user.")
    @commands.has_permissions(administrator=True)
    async def send_embed(ctx, member: discord.Member=None, *, content=None):
        if member is None or not isinstance(member, discord.Member):
            await ctx.send("Invalid user. Please mention a valid user to send an embedded message.", delete_after=10)
            return
        if content is None:
            await ctx.send("Please provide content for the embed in the format: title | body", delete_after=10)
            return

        try:
            title, body = content.split('|', 1)
        except ValueError:
            await ctx.send("Invalid format. Please separate title and body with '|'.", delete_after=10)
            return

        embed = discord.Embed(title=title.strip(), description=body.strip(), color=discord.Color.blue())
        embed.set_footer(text=f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")

        try:
            await member.send(embed=embed)
            await ctx.send(f'Embedded message sent to {member.mention}')
        except discord.HTTPException:
            await ctx.send(f'Failed to send embedded message to {member.mention}', delete_after=10)

    @bot.command(name='say', description="Make the bot repeat a message.")
    async def say(ctx, *, msg=None):
        if msg is None:
            await ctx.send("Please provide a message for the bot to say.", delete_after=10)
            return
        await ctx.send(f'{ctx.author.mention} said: {msg}')

    @bot.command(name='say_embed', description="Make the bot say an embed message.")
    async def say_embed(ctx, *, content=None):
        if content is None:
            await ctx.send("Please provide content for the embed in the format: title | body", delete_after=10)
            return

        try:
            title, body = content.split('|', 1)
        except ValueError:
            await ctx.send("Invalid format. Please separate title and body with '|'.", delete_after=10)
            return

        embed = discord.Embed(title=title.strip(), description=body.strip(), color=discord.Color.blue())
        embed.set_footer(text=f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")

        await ctx.send(embed=embed)

    @kick.error
    @ban.error
    @send.error
    @send_embed.error
    @say_embed.error
    async def error_handler(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the right privileges!", delete_after=10)

# This function should be called in main.py to register the commands
