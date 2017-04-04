import os
import discord
import asyncio
from cogs.utils import checks
from discord.ext import commands
from random import choice, randint
from cogs.utils.dataIO import fileIO

settings = {"Channel": None, "Joinmsg": None, "Leavemsg": None, "Leave": False, "Botrolet": False, "Botrole" : None, "Join": False, "Invites": {}}

class Welcomer:
    def __init__(self, bot):
        self.bot = bot
        self.load = "data/welcomer/settings.json"
        
        
    @commands.group(pass_context=True, no_pm=True)
    async def welcomer(self, ctx):
        """Welcomer modules settings."""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            
    @welcomer.command(pass_context=True)
    async def examples(self, ctx):
        """Shows some examples for settings."""
        msg = """
        Set a message when a user joins
            {0} is the user.
            {1} is the invite.
            {2} is the server.
        Example formats:
            {0.mention} this will mention the user.
            {0.name} this will only say the users name.
            {2.name} is the name of the server
            {1.inviter} is the user that made the invite
            {1.url} is the invite link the user joined with
        Message Examples:
            Join:
                {0.mention} Welcome to {2.name}, User joined with {1.url} referred by {1.inviter}
                Welcome to {2.name} {0.name}! I hope you enjoy your stay! :smile:
            Leave:
                {0.name} has left {2.name}! Oh no we lost a user! :sob:
                Bye bye {0.name}. Hope you had a good stay!
        """
        await self.bot.reply("Here are some examples!")
        await self.bot.type()
        await asyncio.sleep(2)
        await self.bot.say(msg)
        
    @welcomer.command(pass_context=True)
    async def status(self, ctx):
        """Shows the servers settings for welcomer."""
        server = ctx.message.server
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        db = fileIO(self.load, "load")
        e = discord.Embed(colour=discord.Colour(value=color))
        e.set_author(name=server.name, icon_url=server.icon_url)
        e.add_field(name="Server Name:", value=server.name)
        e.add_field(name="Welcomer Channel:", value=db[server.id]["Channel"])
        e.add_field(name="Join Toggle:", value=db[server.id]["Join"])
        e.add_field(name="Leave Toggle:", value=db[server.id]["Leave"])
        e.add_field(name="Bot Role:", value=db[server.id]["Botrole"])
        e.add_field(name="Bot Role Toggle:", value=db[server.id]["Botrolet"])
        e.add_field(name="Join Message:", value=db[server.id]["Joinmsg"], inline=False)
        e.add_field(name="Leave Message:", value=db[server.id]["Leavemsg"], inline=False)
        try:
            await self.bot.say(embed=e)
        except Exception as e:
            await self.bot.say(e)
        
    @welcomer.command(pass_context=True)
    async def channel(self, ctx, *, channel : discord.Channel):
        """Sets the modlog channel setting."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if server.id in db:
            db[server.id]['Channel'] = channel.id
            fileIO(self.load, "save", db)
            await self.bot.say("Channel changed.")
            return
        if not ctx.message.server.me.permissions_in(channel).manage_channels:
            await self.bot.say("I dont have the `manage_channels` permission.")
            return
        if ctx.message.server.me.permissions_in(channel).send_messages:
            if not server.id in db:
                db[server.id] = settings
                db[server.id]['Channel'] = channel.id
                invs = await self.bot.invites_from(server)
                for i in invs:
                    db[server.id]["Invites"][i.url] = i.uses
                fileIO(self.load, "save", db)
                await self.bot.say("Channel set.")
                
    @welcomer.command(pass_context=True)
    async def joinmsg(self, ctx, *, message : str):
        """Sets welcomer joinmsg setting."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if db[server.id]['Joinmsg'] is not None:
            db[server.id]['Joinmsg'] = message
            fileIO(self.load, "save", db)
            await self.bot.say("Join message has been changed.")
        if db[server.id]["Joinmsg"] is None:
            db[server.id]['Joinmsg'] = message
            fileIO(self.load, "save", db)
            await self.bot.say("Join message has been set.")
        else:
            await self.bot.say("Please set the channel you want me to send welcoming and leaving messages to with `{}welcomer channel #channel_name` then you may proceed to setting this message.".format(ctx.prefix))
            
    @welcomer.command(pass_context=True)
    async def leavemsg(self, ctx, *, message : str):
        """Sets the welcomer leavemsg setting."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if db[server.id]['Leavemsg'] is not None:
            db[server.id]['Leavemsg'] = message
            fileIO(self.load, "save", db)
            await self.bot.say("Leave message has been changed.")
        if db[server.id]["Leavemsg"] is None:
            db[server.id]['Leavemsg'] = message
            fileIO(self.load, "save", db)
            await self.bot.say("Leave message has been set.")
        else:
            await self.bot.say("Please set the channel you want me to send welcoming and leaving messages to with `{}welcomer channel #channel_name` then you may proceed to setting this message.".format(ctx.prefix))
        
    @welcomer.command(pass_context=True)
    async def botrole(self, ctx, *, role : discord.Role):
        """Sets the welcomer bot role setting."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if not server.id in db:
            await self.bot.say("Please set the channel you want me to send welcoming and leaving messages to with `{}welcomer channel #channel_name` then you may proceed to setting this message.".format(ctx.prefix))
            return
        if ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            db[server.id]['Botrole'] = role.id
            fileIO(self.load, "save", db)
            await self.bot.say("The bot role has been set.")
        else:
            await self.bot.say("I do not have the `manage_roles` permission!")
        
    @welcomer.command(pass_context=True)
    async def botrolet(self, ctx):
        """Toggles the bot role setting for welcomer."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if not server.id in db:
            await self.bot.say("Please set the channel you want me to send welcoming and leaving messages to with `{}welcomer channel #channel_name` then you may proceed to setting this message.".format(ctx.prefix))
            return
        if db[server.id]['Botrole'] == None:
            await self.bot.say("Botrole not found set it with `{}welcomer botrole`.".format(ctx.prefix))
        if db[server.id]["Botrolet"] == False:
            db[server.id]["Botrolet"] = True
            fileIO(self.load, "save", db)
            await self.bot.say("Bot role enabled.")
        elif db[server.id]["Botrolet"] == True:
            db[server.id]["Botrolet"] = False
            fileIO(self.load, "save", db)
            await self.bot.say("Bot role disabled.")
        
    @welcomer.command(pass_context=True)
    async def togglel(self, ctx):
        """Toggles the leave message for welcomer."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if not server.id in db:
            await self.bot.say("Please set the channel you want me to send welcoming and leaving messages to with `{}welcomer channel #channel_name` then you may proceed to setting this message.".format(ctx.prefix))
            return
        if db[server.id]["Leave"] == False:
            db[server.id]["Leave"] = True
            fileIO(self.load, "save", db)
            await self.bot.say("Leave messages enabled.")
        elif db[server.id]["Leave"] == True:
            db[server.id]["Leave"] = False
            fileIO(self.load, "save", db)
            await self.bot.say("Leave messages disabled.")
            
    @welcomer.command(pass_context=True)
    async def togglej(self, ctx):
        """Toggles the join message for welcomer."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if db[server.id]["Join"] == False:
            db[server.id]["Join"] = True
            fileIO(self.load, "save", db)
            await self.bot.say("Join messages enabled.")
        elif db[server.id]["Join"] == True:
            db[server.id]["Join"] = False
            fileIO(self.load, "save", db)
            await self.bot.say("Join messages disabled.")
        
    @welcomer.command(pass_context=True)
    async def disable(self, ctx):
        """Disables the welcomer."""
        server = ctx.message.server
        db = fileIO(self.load, "load")
        if not server.id in db:
            await self.bot.say("Welcomer was never enabled on this server. :face_palm::drool:")
            return
        del db[server.id]
        fileIO(self.load, "save", db)
        await self.bot.say("Successfully deleted all settings for welcomer for this server.")
        
    async def on_member_join(self, member):
        server = member.server
        db = fileIO(self.load, "load")
        if not server.id in db:
            return
        if member.bot:
            if db[server.id]['Botrolet'] == True:
                roleobj = [r for r in server.roles if r.id == db[server.id]['Botrole']]
                await self.bot.add_roles(member, roleobj[0])
        await asyncio.sleep(1)
        if db[server.id]['Join'] == False:
            return
        channel = db[server.id]["Channel"]
        inv_channel = None
        message = db[server.id]['Joinmsg']
        json_list = db[server.id]["Invites"]
        inv_list = await self.bot.invites_from(server)
        for a in inv_list:
            try:
                if int(a.uses) > int(json_list[a.url]):
                    await self.bot.send_message(server.get_channel(channel), message.format(member, a, server))
            except KeyError:
                await self.bot.send_message(server.get_channel(channel), message.format(member, a, server))
            else:
                pass
        invlist = await self.bot.invites_from(server)
        for i in invlist:
            db[server.id]["Invites"][i.url] = i.uses
        fileIO(self.load, "save", db)
    
    async def on_member_remove(self, member):
        server = member.server
        db = fileIO(self.load, "load")
        if not server.id in db:
            return
        if db[server.id]['Leave'] == False:
            return
        message = db[server.id]['Leavemsg']
        channel = db[server.id]["Channel"]
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
    n = Welcomer(bot)
    bot.add_cog(n)
