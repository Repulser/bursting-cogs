import discord
from __main__ import settings
import asyncio

class reactions:
    def __init__(self, bot):
        self.bot = bot

    async def listener(self, message):
        channel = message.channel
        if message.author.id != self.bot.user.id:
            try:
                if message.content == "lmao":
                    L = "\U0001f1f1"
                    M = "\U0001f1f2"
                    A = "\U0001f1e6"
                    O = "\U0001f1f4"
                    joy = "\U0001f602"
                    cjoy = "\U0001f639"

                    async for x in self.bot.logs_from(channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, L)
                        await self.bot.add_reaction(x, M)
                        await self.bot.add_reaction(x, A)
                        await self.bot.add_reaction(x, O)
                        await self.bot.add_reaction(x, joy)
                        await self.bot.add_reaction(x, cjoy)
                if message.content == "ayy":
                    await self.bot.add_reaction(message, "נ‡±")
                    await self.bot.add_reaction(message, "נ‡²")
                    await self.bot.add_reaction(message, "נ‡¦")
                    await self.bot.add_reaction(message, "נ‡´")
                if message.content == "wew":
                    await self.bot.add_reaction(message, "נ‡±")
                    await self.bot.add_reaction(message, "נ‡¦")
                    await self.bot.add_reaction(message, "נ‡©")
                if message.content == "rekt":
                    R = "\U0001f1f7"
                    E = "\U0001f1ea"
                    K = "\U0001f1f0"
                    T = "\U0001f1f9"
                    FINGERMIDDLE = "\U0001f595"
                    FINGERCROSS = "\U0001f91e"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, R)
                        await self.bot.add_reaction(x, E)
                        await self.bot.add_reaction(x, K)
                        await self.bot.add_reaction(x, T)
                        await self.bot.add_reaction(x, FINGERMIDDLE)
                        await self.bot.add_reaction(x, FINGERCROSS)

                if message.content == "fucker":
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

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, MIDDLEFINGER)
                        await self.bot.add_reaction(x, F)
                        await self.bot.add_reaction(x, U)
                        await self.bot.add_reaction(x, C)
                        await self.bot.add_reaction(x, K)
                        await self.bot.add_reaction(x, E)
                        await self.bot.add_reaction(x, R)
                        await self.bot.add_reaction(x, bump)

                if message.content == "idgaf":
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

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, I)
                        await self.bot.add_reaction(x, D)
                        await self.bot.add_reaction(x, G)
                        await self.bot.add_reaction(x, A)
                        await self.bot.add_reaction(x, F)
                        await self.bot.add_reaction(x, cool)
                        S = "\U0001f1f8"
                if message.content == "sotru":
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

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, S)
                        await self.bot.add_reaction(x, O)
                        await self.bot.add_reaction(x, clap)
                        await self.bot.add_reaction(x, T)
                        await self.bot.add_reaction(x, R)
                        await self.bot.add_reaction(x, U)
                        await self.bot.add_reaction(x, ok)

            except discord.Forbidden:
                pass

def setup(bot):
    n = reactions(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)
