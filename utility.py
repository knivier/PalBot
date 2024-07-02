# utility.py
import discord
from discord.ext import commands
import datetime

def setup_moderation(bot):
    @bot.command(name='kick', description="Kick a user from the server.")
    @commands.has_permissions(administrator=True)
    async def kick(ctx, member: discord.Member=None, *, reason=None):
        if member is None or not isinstance(member, discord.Member):
            await ctx.send("Invalid user. Please mention a valid user to kick.")
            return
        if reason is None:
            await ctx.send("Please provide a reason for kicking this user.")
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
            await ctx.send("Invalid user. Please mention a valid user to ban.")
            return
        if reason is None:
            await ctx.send("Please provide a reason for banning this user.")
            return

        if member.guild != ctx.guild:
            await ctx.send("This user is not a member of this server.")
            return

        try:
            await member.send(f'You have been banned from {ctx.guild.name} for: {reason}')
        except discord.HTTPException:
            pass  # Failed to send a DM, continue anyway

        await member.ban(reason=reason)
        await ctx.send(f'User {member.mention} has been banned for: {reason}')

    @bot.command(name='msg', aliases=['message'], description="Send a direct message to a user.")
    @commands.has_permissions(administrator=True)
    async def message(ctx, member: discord.Member=None, *, msg=None):
        if member is None or not isinstance(member, discord.Member):
            await ctx.send("Invalid user. Please mention a valid user to send a message.")
            return
        if msg is None:
            await ctx.send("Please provide a message to send to the user.")
            return

        try:
            await member.send(f'You have received a message: {msg}')
            await ctx.send(f'Message sent to {member.mention}')
        except discord.HTTPException:
            await ctx.send(f'Failed to send message to {member.mention}')

    @bot.command(name='send_embed', description="Send an embedded message to a user.")
    @commands.has_permissions(administrator=True)
    async def send_embed(ctx, *, content=None):
        if content is None:
            await ctx.send("Please provide content for the embed in the format: title | body")
            return

        try:
            title, body = content.split('|', 1)
        except ValueError:
            await ctx.send("Invalid format. Please separate title and body with '|'.")
            return

        try:
            await ctx.message.delete()  # Delete the command message
        except discord.HTTPException:
            pass

        embed = discord.Embed(title=title.strip(), description=body.strip(), color=discord.Color.blue())
        embed.set_footer(text=f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")

        try:
            await ctx.author.send(embed=embed)  # Send the embed as a DM to the command invoker
            await ctx.send(f'Embedded message sent to {ctx.author.mention}', delete_after=5)  # Delete confirmation message after 5 seconds
        except discord.HTTPException:
            await ctx.send(f'Failed to send embedded message to {ctx.author.mention}')

    @bot.command(name='say', description="Make the bot repeat a message.")
    async def say(ctx, *, msg=None):
        if msg is None:
            await ctx.send("Please provide a message for the bot to say.")
            return
        await ctx.send(f'{ctx.author.mention} said: {msg}')

    @bot.command(name='say_embed', description="Make the bot say an embed message.")
    async def say_embed(ctx, member: discord.Member=None, *, content=None):
        if content is None or member is None or not isinstance(member, discord.Member):
            await ctx.send("Please provide content for the embed in the format: title | body and mention a valid user.")
            return

        try:
            title, body = content.split('|', 1)
        except ValueError:
            await ctx.send("Invalid format. Please separate title and body with '|'.")
            return

        embed = discord.Embed(title=title.strip(), description=body.strip(), color=discord.Color.blue())
        embed.set_footer(text=f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")

        try:
            await member.send(embed=embed)  # Send the embed as a DM to the mentioned user
            await ctx.send(f'Embedded message sent to {member.mention}', delete_after=5)  # Delete confirmation message after 5 seconds
        except discord.HTTPException:
            await ctx.send(f'Failed to send embedded message to {member.mention}')

    @kick.error
    @ban.error
    @message.error
    async def error_handler(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            try:
                await ctx.author.send("You don't have the right privileges!")  # Send error message privately to the command invoker
            except discord.HTTPException:
                pass

# This function should be called in main.py to register the commands
