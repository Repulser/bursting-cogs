import discord
from discord.ext import commands
class teams:
    """Pokemon go teams in discord!"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True, no_pm=True)
    async def valor(self, ctx):
        user = ctx.message.author
        server = ctx.message.server
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        if 'Valor' in roles:
            await self.bot.say("You already joined that team!")
        elif 'Mystic' in roles or 'Instinct' in roles:
            await self.bot.say("You have already joined a team please leave a team before adding a new one")
        else:
            serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
            if 'Mystic' in serverroles and 'Valor' in serverroles and 'Instinct' in serverroles:
                valor = discord.utils.find(lambda r: r.name == 'Valor', ctx.message.server.roles)
                await self.bot.add_roles(user, valor)
                await self.bot.say("Team succesfuly joined! :+1:")

            else:
                await self.bot.say("No roles found, creating them now.... ")
                valor = await self.bot.create_role(ctx.message.server)
                mystic = await self.bot.create_role(ctx.message.server)
                instinct = await self.bot.create_role(ctx.message.server)
                await self.bot.edit_role(ctx.message.server, valor, name='Valor', colour=discord.Colour(value=15995914))
                await self.bot.edit_role(ctx.message.server, mystic, name='Mystic', colour=discord.Colour(value=423919))
                await self.bot.edit_role(ctx.message.server, instinct, name='Instinct', colour=discord.Colour(value=16501507))

    @commands.command(pass_context=True, no_pm=True)
    async def mystic(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        if 'Mystic' in roles:
            await self.bot.say("You already joined that team!")
        elif 'Valor' in roles or 'Instinct' in roles:
            await self.bot.say("You have already joined a team please leave a team before adding a new one")
        else:
            serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
            if 'Mystic' in serverroles and 'Valor' in serverroles and 'Instinct' in serverroles:
                mystic = discord.utils.find(lambda r: r.name == 'Mystic', ctx.message.server.roles)
                await self.bot.add_roles(user, mystic)
                await self.bot.say("Team succesfuly joined! :+1:")

            else:
                await self.bot.say("No roles found, creating them now.... ")
                valor = await self.bot.create_role(ctx.message.server)
                mystic = await self.bot.create_role(ctx.message.server)
                instinct = await self.bot.create_role(ctx.message.server)
                await self.bot.edit_role(ctx.message.server, valor, name='Valor', colour=discord.Colour(value=15995914))
                await self.bot.edit_role(ctx.message.server, mystic, name='Mystic', colour=discord.Colour(value=423919))
                await self.bot.edit_role(ctx.message.server, instinct, name='Instinct', colour=discord.Colour(value=16501507))

    @commands.command(pass_context=True, no_pm=True)
    async def instinct(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        if 'Instinct' in roles:
            await self.bot.say("You already joined that team!")
        elif 'Mystic' in roles or 'Valor' in roles:
            await self.bot.say("You have already joined a team please leave a team before adding a new one")
        else:
            serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
            if 'Mystic' in serverroles and 'Valor' in serverroles and 'Instinct' in serverroles:
                instinct = discord.utils.find(lambda r: r.name == 'Instinct', ctx.message.server.roles)
                await self.bot.add_roles(user, instinct)
                await self.bot.say("Team succesfuly joined! :+1:")

            else:
                await self.bot.say("No roles found, creating them now.... ")
                valor = await self.bot.create_role(ctx.message.server)
                mystic = await self.bot.create_role(ctx.message.server)
                instinct = await self.bot.create_role(ctx.message.server)
                await self.bot.edit_role(ctx.message.server, valor, name='Valor', colour=discord.Colour(value=15995914))
                await self.bot.edit_role(ctx.message.server, mystic, name='Mystic', colour=discord.Colour(value=423919))
                await self.bot.edit_role(ctx.message.server, instinct, name='Instinct', colour=discord.Colour(value=16501507))
    @commands.group(name= 'teamleave', pass_context=True, no_pm=True)
    async def _teamleave(self, ctx):
        """Leave a pokemon go team"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            return

    @_teamleave.command(name = 'valor', pass_context=True, no_pm=True)
    async def _valor(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        valor = discord.utils.find(lambda r: r.name == 'Valor', ctx.message.server.roles)
        if 'Mystic' in serverroles and 'Valor' in serverroles and 'Instinct' in serverroles:
            if 'Valor' in roles:
                await self.bot.remove_roles(user, valor)
                await self.bot.say("Succesfuly left team :+1:")
            else:
                await self.bot.say("You have not joined that team!")
        else:
            await self.bot.say("Please run the join command for first time configuration")
    @_teamleave.command(name = 'mystic', pass_context=True, no_pm=True)
    async def _mystic(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        valor = discord.utils.find(lambda r: r.name == 'Mystic', ctx.message.server.roles)
        if 'Mystic' in serverroles and 'Valor' in serverroles and 'Instinct' in serverroles:
            if 'Mystic' in roles:
                await self.bot.remove_roles(user, valor)
                await self.bot.say("Succesfuly left team :+1:")
            else:
                await self.bot.say("You have not joined that team!")
        else:
            await self.bot.say("Please run the join command for first time configuration")

    @_teamleave.command(name = 'instinct', pass_context=True, no_pm=True)
    async def _instinct(self, ctx):
        server = ctx.message.server
        user = ctx.message.author
        serverroles = [role.name.replace('@', '@\u200b') for role in server.roles]
        roles = [role.name.replace('@', '@\u200b') for role in user.roles]
        valor = discord.utils.find(lambda r: r.name == 'Instinct', ctx.message.server.roles)
        if 'Mystic' in serverroles and 'Valor' in serverroles and 'Instinct' in serverroles:
            if 'Instinct' in roles:
                await self.bot.remove_roles(user, valor)
                await self.bot.say("Succesfuly left team  :+1:")
            else:
                await self.bot.say("You have not joined that team!")
        else:
            await self.bot.say("Please run the join command for first time configuration")

def setup(bot):
    n = teams(bot)
    bot.add_cog(n)
