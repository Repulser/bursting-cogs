import discord
import asyncio
from discord.ext import commands
import cleverbot
class talk:
    """Talk with the bot!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def talk(self, ctx):
        cleverbot_client = cleverbot.Cleverbot()
        await self.bot.say(":fire: type exit to quit")
        while True:
            question = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel, timeout = 60)
            try:
                if question.content == "exit":
                    await self.bot.say(":+1:")
                    break
                await self.bot.send_typing(ctx.message.channel)
                answer = cleverbot_client.ask(question.content)
                await asyncio.sleep(2)
                await self.bot.say(answer)
            except AttributeError:
                await self.bot.say("Ok then, well talk later")
                break

def setup(bot):
    n = talk(bot)
    bot.add_cog(n)
