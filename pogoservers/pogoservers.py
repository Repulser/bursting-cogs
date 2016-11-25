import requests
import discord
from discord.ext import commands
from random import choice, randint
from bs4 import BeautifulSoup
class pogo:
    """pogo"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def pogoservers(self, ctx):
        url = "http://cmmcd.com/PokemonTrainerClub/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        links = soup.find_all('font')
        for item in links:
            level = item.text
        url = "http://cmmcd.com/PokemonGo/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        links = soup.find_all('font')
        for item in links:
            level2 = item.text
        r = requests.get("https://pgorelease.nianticlabs.com/plfe/version")
        soup = BeautifulSoup(r.content, "html.parser")
        x = r.content
        decoded = x.decode("utf-8")[2:]
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        data = discord.Embed(description=level, colour=discord.Colour(value=color))
        data.add_field(name="Pokémon Go Server Status", value=level2)
        listd = list(decoded)
        if listd[0] != "t":
            data.add_field(name="Api version", value=decoded)
        data.set_author(name="PTC Login status")
        await self.bot.say(embed=data)


def setup(bot):
    n = pogo(bot)
    bot.add_cog(n)
