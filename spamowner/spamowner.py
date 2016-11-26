import discord
from .utils import checks
from __main__ import settings
from discord.ext import commands

class spam:
    """Spams."""

    def __init__(self, bot):
        self.bot = bot
    @checks.is_owner()
    @commands.command(pass_context = True)
    async def spam(self, ctx, user : discord.Member, spamtext, number : int=None):
        """Spams x times, default is 10."""
        if user.id == "96987941519237120" or user.id == "166179284266778624":
            await self.bot.say("Hell nah, I ain't spamming him.")
            return
        if number == None:
            number = 10
        counter = 0
        while counter < number:
            await self.bot.send_message(user, "{}, sent by **{}**.".format(spamtext, ctx.message.author))
            counter = counter + 1
            if counter == 1:
                await self.bot.say("Hehe, {} got spammed {} time!".format(user.mention, counter))
            else:
                await self.bot.say("Hehe, {} got spammed {} times!".format(user.mention, counter))
    @checks.is_owner()
    @commands.command(hidden=True)
    async def aspam(self, user : discord.Member, spamtext, number : int=None):
        """Spams x times anonymously, default is 10."""
        if user.id == "96987941519237120" or user.id == "166179284266778624":
            await self.bot.say("Hell nah, I ain't spamming him.")
            return
        if number == None:
            number = 10
        counter = 0
        await self.bot.delete_message(ctx.message)
        while counter < number:
            await self.bot.send_message(user, "{}".format(spamtext))
            counter = counter + 1
    @checks.is_owner()
    @commands.command(pass_context = True)
    async def cspam(self, ctx, spamtext, number : int=None):
        """Spams x times in the channel, default is 10."""
        if number == None:
            number = 10
        counter = 0
        while counter < number:
            await self.bot.say("{}, sent by **{}**.".format(spamtext, ctx.message.author))
            counter = counter + 1  
    @checks.is_owner()
    @commands.command(pass_context = True)
    async def acspam(self, ctx, spamtext, number : int=None):
        """Spams x times in the channel anonymously, default is 10."""
        if number == None:
            number = 10
        counter = 0
        await self.bot.delete_message(ctx.message)
        while counter < number:
            await self.bot.say("{}".format(spamtext))
            counter = counter + 1  

def setup(bot):
    bot.add_cog(spam(bot))
