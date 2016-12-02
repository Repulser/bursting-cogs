import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks
class disco:
    """Disco role"""

    def __init__(self, bot):
        self.bot = bot
    @checks.mod_or_permissions(moderator=True)
    @commands.command(pass_context = True, no_pm=True)
    async def discorole(self, ctx, times : int, role: discord.Role, interval : float):
        time = 0
        while time < times:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, role, colour=discord.Colour(value=colour))
            time = time + 1
            await asyncio.sleep(interval)
	
    @checks.mod_or_permissions(moderator=True)
    @commands.command(pass_context = True, no_pm=True)
    async def discoroleforever(self, ctx, role: discord.Role, interval : float):
        
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, role, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)


def setup(bot):
    n = disco(bot)
    bot.add_cog(n)
