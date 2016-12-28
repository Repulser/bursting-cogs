from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO
import discord
import asyncio
import os
from random import choice, randint

inv_settings = {"Channel": None, "joinmessage": None, "leavemessage": None, "Embed": False, "leave": False, "botroletoggle": False, "botrole" : None, "join": False, "Invites": {}}


class invitemirror:
    def __init__(self, bot):
        self.bot = bot
        self.direct = "data/welcomer/settings.json"

    @checks.admin_or_permissions(administrator=True)
    @commands.group(name='welcomer', pass_context=True, no_pm=True)
    async def welcome(self, ctx):
        """Welcome and leave message, with invite link. Make sure to start first by settings the welcomer joinmessage, then continue to toggle, set leave ETC"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @welcome.command(name='joinmessage', pass_context=True, no_pm=True)
    async def joinmessage(self, ctx, *, message: str):
        """
        Set a message when a user joins
        {0} is the user
        {1} is the invite that he/her joined using
        {2} is the server {2.name} <-
        Example formats:
            {0.mention} this will mention the user when he joins
            {2.name} is the name of the server
            {1.inviter} is the user that made the invite
            {1.url} is the invite link the user joined with
        Message Examples:
        {0.mention} Welcome to {2.name}, User joined with {1.url} referred by {1.inviter}
        Welcome to {2.name} {0}! I hope you enjoy your stay
        """
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if server.id in db:
            db[server.id]['joinmessage'] = message
            fileIO(self.direct, "save", db)
            await self.bot.say("Join message changed.")
            return
        if not ctx.message.server.me.permissions_in(ctx.message.channel).manage_channels:
            await self.bot.say("I dont have the manage channels permission.")
            return
        if ctx.message.server.me.permissions_in(ctx.message.channel).send_messages:
            if not server.id in db:
                db[server.id] = inv_settings
                db[server.id]['joinmessage'] = message
                invlist = await self.bot.invites_from(server)
                db[server.id]["Channel"] = ctx.message.channel.id
                for i in invlist:
                    db[server.id]["Invites"][i.url] = i.uses
                fileIO(self.direct, "save", db)
                await self.bot.say("I will now send welcome notifications here (If toggled)")
        else:
            return

    @welcome.command(name='leavemessage', pass_context=True, no_pm=True)
    async def leavemessage(self, ctx, *, message: str):
        """
        Set a message when a user leaves
        {0} is the user
        {1} is the server
        Example formats:
            {0.mention} this will mention the user when he joins
            {1.name} is the name of the server
            {0.name} is the name
        Message Examples:
            {0.mention} Welcome to {1.name}
            Welcome to {1.name} {0}! I hope you enjoy your stay
        """
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if server.id in db:
            db[server.id]['leavemessage'] = message
            fileIO(self.direct, "save", db)
            await self.bot.say("Leave message changed.")
            return
        if ctx.message.server.me.permissions_in(ctx.message.channel).send_messages:
            if not server.id in db:
                db[server.id]['leavemessage'] = message
                db[server.id]["Channel"] = ctx.message.channel.id
                fileIO(self.direct, "save", db)
                await self.bot.say("I will now send leave notifications here (If toggled)")

    @welcome.command(name='botrole', pass_context=True, no_pm=True)
    async def botrole(self, ctx, *, role : discord.Role):
        """sets the botrole to auto assign roles to bots"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            await self.bot.say("Server not found, use welcomer joinmessage to set a channel.")
            return
        if ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            db[server.id]['botrole'] = role.id
            fileIO(self.direct, "save", db)
            await self.bot.say("Bot role saved")
        else:
            await self.bot.say("I do not have the manage_roles permission")

    @welcome.command(name='botroletoggle', pass_context=True, no_pm=True)
    async def botroletoggle(self, ctx):
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            await self.bot.say("Server not found, use welcomer joinmessage to set a channel.")
            return
        if db[server.id]['botrole'] == None:
            await self.bot.say("Botrole not found set it with welcomer botrole")
        if db[server.id]["botroletoggle"] == False:
            db[server.id]["botroletoggle"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Bot role enabled")
        elif db[server.id]["botroletoggle"] == True:
            db[server.id]["botroletoggle"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Bot roledisabled")


    @welcome.command(name='toggleleave', pass_context=True, no_pm=True)
    async def toggleleave(self, ctx):
        """toggle leave message"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["leave"] == False:
            db[server.id]["leave"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Leave messages enabled")
        elif db[server.id]["leave"] == True:
            db[server.id]["leave"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Leave messages disabled")

    @welcome.command(name='togglejoin', pass_context=True, no_pm=True)
    async def togglejoin(self, ctx):
        """toggle join message"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["join"] == False:
            db[server.id]["join"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Join messages enabled")
        elif db[server.id]["join"] == True:
            db[server.id]["join"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Join messages disabled")

    @welcome.command(name='embed', pass_context=True, no_pm=True)
    async def embed(self, ctx):
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            await self.bot.say("Server not found, use welcomer joinmessage to set a channel.")
            return
        if db[server.id]["Embed"] == False:
            db[server.id]["Embed"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Embeds enabled")
        elif db[server.id]["Embed"] == True:
            db[server.id]["Embed"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Embeds disabled")

    @welcome.command(name='disable', pass_context=True, no_pm=True)
    async def disable(self, ctx):
        """disables the welcomer"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            await self.bot.say("Server not found, use welcomer joinmessage to set a channel.")
            return
        del db[server.id]
        fileIO(self.direct, "save", db)
        await self.bot.say("I will no longer send welcomer notifications here")

    async def on_member_join(self, member):
        server = member.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if member.bot:
            if db[server.id]['botroletoggle'] == True:
                roleobj = [r for r in server.roles if r.id == db[server.id]['botrole']]
                await self.bot.add_roles(member, roleobj[0])
        await asyncio.sleep(1)
        if db[server.id]['join'] == False:
            return
        channel = db[server.id]["Channel"]
        inv_channel = None
        message = db[server.id]['joinmessage']
        json_list = db[server.id]["Invites"]
        inv_list = await self.bot.invites_from(server)
        for a in inv_list:
            try:
                if int(a.uses) > int(json_list[a.url]):
                    if db[server.id]["Embed"] == True:
                        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
                        color = int(color, 16)
                        data = discord.Embed(title="ID: {}".format(member.id),
                                             description=message.format(member, a, server),
                                             colour=discord.Colour(value=color))
                        data.set_thumbnail(url=member.avatar_url)
                        await self.bot.send_message(server.get_channel(channel), embed=data)
                    else:
                        await self.bot.send_message(server.get_channel(channel), message.format(member, a, server))
            except KeyError:
                if db[server.id]["Embed"] == True:
                    color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
                    color = int(color, 16)
                    data = discord.Embed(title="ID: {}".format(member.id),
                                         description=message.format(member, a, server),
                                         colour=discord.Colour(value=color))
                    data.set_thumbnail(url=member.avatar_url)
                    await self.bot.send_message(server.get_channel(channel), embed=data)
                else:
                    await self.bot.send_message(server.get_channel(channel), message.format(member, a, server))
                break
            else:
                pass
        invlist = await self.bot.invites_from(server)
        for i in invlist:
            db[server.id]["Invites"][i.url] = i.uses
        fileIO(self.direct, "save", db)

    async def on_member_remove(self, member):
        server = member.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if db[server.id]['leave'] == False:
            return
        message = db[server.id]['leavemessage']
        channel = db[server.id]["Channel"]
        if db[server.id]["Embed"] == True:
            color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            data = discord.Embed(title="ID: {}".format(member.id),
                                 description=message.format(member, server),
                                 colour=discord.Colour(value=color))
            data.set_thumbnail(url=member.avatar_url)
            await self.bot.send_message(server.get_channel(channel), embed=data)
        else:
            await self.bot.send_message(server.get_channel(channel), message.format(member, server))


def check_folder():
    if not os.path.exists('data/welcomer'):
        print('Creating data/welcomer folder...')
        os.makedirs('data/welcomer')


def check_file():
    f = 'data/welcomer/settings.json'
    if not fileIO(f, 'check'):
        print('Creating default settings.json...')
        fileIO(f, 'save', {})


def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(invitemirror(bot))
