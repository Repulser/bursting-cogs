import discord
from discord.ext import commands
from cogs.utils import checks
import asyncio
import string
class react:
    """reactions!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, no_pm=True)
    async def reactlist(self, ctx):
        data = discord.Embed(description="\nlmao\nrekt\nlitaf\nsotru\nfucker\nnoscope\nidgaf\nreact\nidgaf - Custom reaction")
        data.set_author(name="Reaction commands:")
        await self.bot.say(embed=data)
    @commands.command(pass_context = True, no_pm=True)
    async def emojireact(self, ctx, emojis):
        async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                emolist = list(emojis)
                for item in emolist:
                    await self.bot.add_reaction(x, item)

    @commands.command(pass_context = True, no_pm=True)
    async def react(self, ctx, *, reaction):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            reaction = reaction.upper()
            dictionary = { "A" : "\U0001f1e6", "B": "\U0001f1e7", "C": "\U0001f1e8", "D": "\U0001f1e9", "E":  "\U0001f1ea", "F": "\U0001f1eb", "G": "\U0001f1ec", "H" : "\U0001f1ed", "I": "\U0001f1ee", "J": "\U0001f1ef", "K" : "\U0001f1f0", "L": "\U0001f1f1", "M" : "\U0001f1f2", "N" : "\U0001f1f3", "O" : "\U0001f1f4", "P" : "\U0001f1f5", "Q" : "\U0001f1f6",  "R" : "\U0001f1f7", "S" : "\U0001f1f8", "T" : "\U0001f1f9", "U" : "\U0001f1fa", "V" : "\U0001f1fb", "W" : "\U0001f1fc", "X" : "\U0001f1fd", "Y" : "\U0001f1fe", "Z" : "\U0001f1ff"}
            a = reaction
            try:
                listr = [dictionary[char] for char in a]
                dontrun = False
            except KeyError:
                dontrun = True
            lenstr = len(reaction)
            if lenstr > 12:
                await self.bot.say("Length cannot be more than 12 characters")
            elif dontrun == True:
                await self.bot.say("Could not find, letters only")
            elif lenstr == 12:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                        await self.bot.add_reaction(x, listr[6])
                        await self.bot.add_reaction(x, listr[7])
                        await self.bot.add_reaction(x, listr[8])
                        await self.bot.add_reaction(x, listr[9])
                        await self.bot.add_reaction(x, listr[10])
                        await self.bot.add_reaction(x, listr[11])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")
            elif lenstr == 11:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                        await self.bot.add_reaction(x, listr[6])
                        await self.bot.add_reaction(x, listr[7])
                        await self.bot.add_reaction(x, listr[9])
                        await self.bot.add_reaction(x, listr[10])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")
            elif lenstr == 10:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                        await self.bot.add_reaction(x, listr[6])
                        await self.bot.add_reaction(x, listr[7])
                        await self.bot.add_reaction(x, listr[8])
                        await self.bot.add_reaction(x, listr[9])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")
            elif lenstr == 9:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                        await self.bot.add_reaction(x, listr[6])
                        await self.bot.add_reaction(x, listr[7])
                        await self.bot.add_reaction(x, listr[8])

                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")

            elif lenstr == 8:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                        await self.bot.add_reaction(x, listr[6])
                        await self.bot.add_reaction(x, listr[7])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")
            elif lenstr == 7:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                        await self.bot.add_reaction(x, listr[6])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")

            elif lenstr == 6:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                        await self.bot.add_reaction(x, listr[5])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")
            elif lenstr == 5:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                        await self.bot.add_reaction(x, listr[4])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")

            elif lenstr == 4:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                        await self.bot.add_reaction(x, listr[3])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")

            elif lenstr == 3:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                        await self.bot.add_reaction(x, listr[2])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")

            elif lenstr == 2:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                        await self.bot.add_reaction(x, listr[1])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")
            elif lenstr == 1:
                async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                    try:
                        await self.bot.add_reaction(x, listr[0])
                    except KeyError:
                        await self.bot.say("Could not find, Letters only and caps.")

            else:
                await self.bot.say("Fatal error")

    @commands.command(pass_context = True, no_pm=True)
    async def litaf(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            L = "\U0001f1f1"
            I = "\U0001f1ee"
            T = "\U0001f1f9"
            fire = "\U0001f525"
            A = "\U0001f1e6"
            F = "\U0001f1eb"
            ok = "\U0001f44c"

        async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, L)
                await self.bot.add_reaction(x, I)
                await self.bot.add_reaction(x, T)
                await self.bot.add_reaction(x, fire)
                await self.bot.add_reaction(x, A)
                await self.bot.add_reaction(x, F)
                await self.bot.add_reaction(x, ok)

    @commands.command(pass_context = True, no_pm=True)
    async def sotru(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            S = "\U0001f1f8"
            U = "\U0001f1fa"
            O = "\U0001f1f4"
            R = "\U0001f1f7"
            L = "\U0001f1f1"
            I = "\U0001f1ee"
            T = "\U0001f1f9"
            fire = "\U0001f525"
            A = "\U0001f1e6"
            F = "\U0001f1eb"
            ok = "\U0001f44c"
            clap = "\U0001f44f"

            async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, S)
                await self.bot.add_reaction(x, O)
                await self.bot.add_reaction(x, clap)
                await self.bot.add_reaction(x, T)
                await self.bot.add_reaction(x, R)
                await self.bot.add_reaction(x, U)
                await self.bot.add_reaction(x, ok)
    @commands.command(pass_context = True, no_pm=True)
    async def idgaf(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            S = "\U0001f1f8"
            U = "\U0001f1fa"
            D = "\U0001f1e9"
            G = "\U0001f1ec"
            O = "\U0001f1f4"
            R = "\U0001f1f7"
            L = "\U0001f1f1"
            I = "\U0001f1ee"
            T = "\U0001f1f9"
            fire = "\U0001f525"
            A = "\U0001f1e6"
            F = "\U0001f1eb"
            ok = "\U0001f44c"
            clap = "\U0001f44f"
            cool = "\U0001f60e"

            async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, I)
                await self.bot.add_reaction(x, D)
                await self.bot.add_reaction(x, G)
                await self.bot.add_reaction(x, A)
                await self.bot.add_reaction(x, F)
                await self.bot.add_reaction(x, cool)
    @commands.command(pass_context = True, no_pm=True)
    async def lmao(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            L = "\U0001f1f1"
            M = "\U0001f1f2"
            A = "\U0001f1e6"
            O = "\U0001f1f4"
            joy = "\U0001f602"
            cjoy = "\U0001f639"

            async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, L)
                await self.bot.add_reaction(x, M)
                await self.bot.add_reaction(x, A)
                await self.bot.add_reaction(x, O)
                await self.bot.add_reaction(x, joy)
                await self.bot.add_reaction(x, cjoy)

    @commands.command(pass_context = True, no_pm=True)
    async def rekt(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            R = "\U0001f1f7"
            E = "\U0001f1ea"
            K = "\U0001f1f0"
            T = "\U0001f1f9"
            FINGERMIDDLE = "\U0001f595"
            FINGERCROSS = "\U0001f91e"

            async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, R)
                await self.bot.add_reaction(x, E)
                await self.bot.add_reaction(x, K)
                await self.bot.add_reaction(x, T)
                await self.bot.add_reaction(x, FINGERMIDDLE)
                await self.bot.add_reaction(x, FINGERCROSS)

    @commands.command(pass_context = True, no_pm=True)
    async def noscope(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            N = "\U0001f1f3"
            BOOM = "\U0001f4a5"
            S = "\U0001f1f8"
            C = "\U0001f595"
            O = "\U0001f1f4"
            P = "\U0001f1f5"
            E = "\U0001f1ea"
            GLASSES = "\U0001f576"

            async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, N)
                await self.bot.add_reaction(x, O)
                await self.bot.add_reaction(x, BOOM)
                await self.bot.add_reaction(x, S)
                await self.bot.add_reaction(x, C)
                await self.bot.add_reaction(x, O)
                await self.bot.add_reaction(x, P)
                await self.bot.add_reaction(x, E)
                await self.bot.add_reaction(x, GLASSES)

    @commands.command(pass_context = True, no_pm=True)
    async def fucker(self, ctx):
        try:
            await self.bot.delete_message(ctx.message)
        finally:
            MIDDLEFINGER = "\U0001f595"
            F = "\U0001f1eb"
            U = "\U0001f1fa"
            C = "\U0001f1e8"
            K = "\U0001f1f0"
            Y = "\U0001f1fe"
            O = "\U0001f1f4"
            E = "\U0001f1ea"
            R = "\U0001f1f7"
            point = "\U0001f446"
            FIST = "\U0001f91c"
            bump = "\U0001f91b"

            async for x in self.bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=1):
                await self.bot.add_reaction(x, MIDDLEFINGER)
                await self.bot.add_reaction(x, F)
                await self.bot.add_reaction(x, U)
                await self.bot.add_reaction(x, C)
                await self.bot.add_reaction(x, K)
                await self.bot.add_reaction(x, E)
                await self.bot.add_reaction(x, R)
                await self.bot.add_reaction(x, bump)

def setup(bot):
    n = react(bot)
    bot.add_cog(n)
