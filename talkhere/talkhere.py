import discord
from discord.ext import commands
import cleverbot
import random
import asyncio
class talk:
    """Talk with the bot!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def talkhere(self, ctx):
        cleverbot_client = cleverbot.Cleverbot()
        await self.bot.say("Person 2: Hi")
        first = cleverbot_client.ask("Hi")
        p1 = "Hi"
        p2 = "Hello"
        p3 = "How are you"
        choices = [1, 2, 3]
        while True:
            choice = random.choice(choices)
            if choice == 1:
                asyncio.sleep(0.5)
                p1 = cleverbot_client.ask(first)
                await self.bot.say("Person 1: {}".format(p1))
            elif choice == 2:
                asyncio.sleep(0.5)
                p2 = cleverbot_client.ask(p1)
                await self.bot.say("Person 2: {}".format(p2))
            elif choice == 3:
                asyncio.sleep(0.5)
                p3 = cleverbot_client.ask(p1)
                await self.bot.say("Person 3: {}".format(p3))

def setup(bot):
    n = talk(bot)
    bot.add_cog(n)
