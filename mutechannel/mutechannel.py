import requests
import asyncio
import discord
from discord.ext import commands
from random import choice, randint
from bs4 import BeautifulSoup
class channelmute:
    """Channel mute"""

    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context = True)
    async def mutechannel(self, ctx):
        perms = discord.PermissionOverwrite()
        perms.send_messages = False
        await self.bot.edit_channel_permissions(ctx.message.channel, ctx.message.server.default_role ,perms)
        todelete = await self.bot.say("Done :+1:")
        await asyncio.sleep(5)
        await self.bot.delete_message(todelete)

def setup(bot):
    n = channelmute(bot)
    bot.add_cog(n)
