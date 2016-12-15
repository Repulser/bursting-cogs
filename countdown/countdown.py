from discord.ext import commands
import asyncio
class countdown:
    """Countdown timer!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def countdown(self, ctx, seconds, title):
        counter = 0
        try:
            secondint = int(seconds)
            message = await self.bot.say("```css" + "\n" + "[" + title +"]" + "\nTimer: " + seconds + "```")
            while True:
                secondint = secondint - 1
                if secondint == 0:
                    await self.bot.edit_message(message, new_content=("```Ended!```"))
                    break
                await self.bot.edit_message(message, new_content=("```css" + "\n" + "[" + title + "]" + "\nTimer: {0}```".format(secondint)))
                await asyncio.sleep(1)
            await self.bot.send_message(ctx.message.channel, ctx.message.author.mention + " Your countdown " + "[" + title + "]"  + " Has ended!")
        except ValueError:
            await self.bot.say("Must be a number!")


def setup(bot):
    n = countdown(bot)
    bot.add_cog(n)
