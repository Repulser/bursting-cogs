import discord
from discord.ext import commands
from cogs.utils import checks

class repeat:
    """Bot repeats what you say."""

    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(pass_context = True)
    async def monkeysee(self, ctx):
        channel = ctx.message.channel
        author = ctx.message.author
        await self.bot.send_message(channel, "Monkeydo, type exit to stop")
        while True:
            torepeat = await self.bot.wait_for_message(author=author, channel=channel, timeout = None)
            await self.bot.send_message(channel, torepeat.content)
            if torepeat.content == "exit":
                break


def setup(bot):
    n = repeat(bot)
    bot.add_cog(n)

