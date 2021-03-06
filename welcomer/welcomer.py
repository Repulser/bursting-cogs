import os
import discord
import asyncio
from cogs.utils import checks
from discord.ext import commands
from random import choice, randint
from cogs.utils.dataIO import dataIO

settings = {"Channel": None, "Embed": False, "joinmessage": None, "leavemessage": None, "leave": False,
            "botroletoggle": False, "botrole": None, "join": False, "Invites": {}}


class Welcomer:
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "data/welcomer/settings.json"
        self.config = dataIO.load_json(self.config_file)

    @commands.group(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_server=True)
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
    join:
        {0.mention} Welcome to {2.name}, User joined with {1.url} referred by {1.inviter} Welcome to {2.name} {0.name}! I hope you enjoy your stay!
    leave:
        {0.name} has left {2.name}! Oh no we lost a user! Bye bye {0.name}. Hope you had a good stay!"""
        await self.bot.say("**Here are some examples!**\n\n" + "```css\n" + msg + "```")

    @welcomer.command(pass_context=True)
    async def status(self, ctx):
        """Shows the servers settings for welcomer."""
        if ctx.message.server.id not in self.config:
            await self.bot.say(":x: **Welcomer has not been configured for this server, use `welcomer channel` first**")
            return
        server = ctx.message.server
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        e = discord.Embed(colour=discord.Colour(value=color), description="\n\a")
        role = discord.utils.get(ctx.message.server.roles, id=self.config[server.id]["botrole"])
        e.set_author(name="Settings for " + server.name, icon_url=server.icon_url)
        e.add_field(name="Welcomer Channel:",
                    value="#" + self.bot.get_channel(self.config[server.id]["Channel"]).name if self.bot.get_channel(
                        self.config[server.id]["Channel"]) else None, inline=True)
        e.add_field(name="Join Toggle:", value=self.config[server.id]["join"], inline=True)
        e.add_field(name="Leave Toggle:", value=self.config[server.id]["leave"], inline=True)
        e.add_field(name="Bot Role:", value=role.name if role else None)
        e.add_field(name="Bot Role Toggle:", value=self.config[server.id]["botroletoggle"])
        e.add_field(name="Embed", value=self.config[server.id]["Embed"], inline=True)
        e.add_field(name="Leave Message:", value=self.config[server.id]["leavemessage"], inline=False)
        e.add_field(name="Join Message:", value=self.config[server.id]["joinmessage"], inline=False)
        try:
            await self.bot.say(embed=e)
        except Exception as e:
            await self.bot.say(e)

    @welcomer.command(pass_context=True)
    async def channel(self, ctx, *, channel: discord.Channel = None):
        """Sets the welcomer channel settings."""
        if channel is None:
            channel = ctx.message.channel
        server = ctx.message.server
        if server.id in self.config:
            self.config[server.id]['Channel'] = channel.id
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("Channel changed.")
            return
        if not ctx.message.server.me.permissions_in(channel).manage_channels:
            await self.bot.say("I dont have the `manage_channels` permission.")
            return
        if ctx.message.server.me.permissions_in(channel).send_messages:
            if server.id not in self.config:
                self.config[server.id] = settings
                self.config[server.id]['Channel'] = channel.id
                invs = await self.bot.invites_from(server)
                for i in invs:
                    self.config[server.id]["Invites"][i.url] = i.uses
                dataIO.save_json(self.config_file, self.config)
                await self.bot.say("Channel set.")

    @welcomer.command(pass_context=True)
    async def joinmessage(self, ctx, *, message: str):
        """Sets welcomer joinmessage setting."""
        server = ctx.message.server
        if ctx.message.server.id not in self.config:
            await self.bot.say(
                ":x: **Please set the channel you want me to send welcoming and leaving messages to with `welcomer "
                "channel #channel_name` then you may proceed to setting this message..**")
            return
        if self.config[server.id]['joinmessage'] is not None:
            self.config[server.id]['joinmessage'] = message
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("join message has been changed.")
        elif self.config[server.id]["joinmessage"] is None:
            self.config[server.id]['joinmessage'] = message
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("Join message has been set.")

    @welcomer.command(pass_context=True)
    async def leavemessage(self, ctx, *, message: str):
        """Sets the welcomer leavemessage setting."""
        server = ctx.message.server
        if ctx.message.server.id not in self.config:
            await self.bot.say(
                ":x: **Please set the channel you want me to send welcoming and leaving messages to with `welcomer "
                "channel #channel_name` then you may proceed to setting this message..**")
            return
        if self.config[server.id]['leavemessage'] is not None:
            self.config[server.id]['leavemessage'] = message
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("leave message has been changed.")
        elif self.config[server.id]["leavemessage"] is None:
            self.config[server.id]['leavemessage'] = message
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("leave message has been set.")

    @welcomer.command(pass_context=True)
    async def botrole(self, ctx, *, role: discord.Role):
        """Sets the welcomer bot role setting."""
        server = ctx.message.server
        if server.id not in self.config:
            await self.bot.say(
                ":x: **Please set the channel you want me to send welcoming and leaving messages to with\n`welcomer "
                "channel #channel_name`\nthen you may proceed to setting this message.**")
            return
        if ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            self.config[server.id]['botrole'] = role.id
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("The bot role has been set.")
        else:
            await self.bot.say("I do not have the `manage_roles` permission!")

    @welcomer.command(pass_context=True)
    async def botroletoggle(self, ctx):
        """Toggles the bot role setting for welcomer."""
        server = ctx.message.server
        if server.id not in self.config:
            await self.bot.say(
                ":x: **Please set the channel you want me to send welcoming and leaving messages to with\n`welcomer "
                "channel #channel_name`\nthen you may proceed to setting this message.**")
            return
        if self.config[server.id]['botroletoggle'] is None:
            await self.bot.say("botroletoggle not found set it with `{}welcomer botroletoggle`.".format(ctx.prefix))
        if self.config[server.id]["botroletoggle"] is False:
            self.config[server.id]["botroletoggle"] = True
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("Bot role enabled.")
        elif self.config[server.id]["botroletoggle"] is True:
            self.config[server.id]["botroletoggle"] = False
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("Bot role disabled.")

    @welcomer.command(pass_context=True)
    async def embed(self, ctx):
        """Toggles the bot role setting for welcomer."""
        server = ctx.message.server
        if server.id not in self.config:
            await self.bot.say(
                "**Please set the channel you want me to send welcoming and leaving messages to with `welcomer "
                "channel #channel_name` then you may proceed to setting this message.**")
            return
        if self.config[server.id]["Embed"] is False:
            self.config[server.id]["Embed"] = True
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("Embeds enabled")
        elif self.config[server.id]["Embed"] is True:
            self.config[server.id]["Embed"] = False
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("Embeds disabled")

    @welcomer.command(pass_context=True)
    async def togglel(self, ctx):
        """Toggles the leave message for welcomer."""
        server = ctx.message.server
        if server.id not in self.config:
            await self.bot.say(
                "**Please set the channel you want me to send welcoming and leaving messages to with `welcomer "
                "channel #channel_name` then you may proceed to setting this message.**")
            return
        if self.config[server.id]["leave"] is False:
            self.config[server.id]["leave"] = True
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("leave messages enabled.")
        elif self.config[server.id]["leave"] is True:
            self.config[server.id]["leave"] = False
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("leave messages disabled.")

    @welcomer.command(pass_context=True)
    async def togglej(self, ctx):
        """Toggles the join message for welcomer."""
        server = ctx.message.server
        if self.config[server.id]["join"] is False:
            self.config[server.id]["join"] = True
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("join messages enabled.")
        elif self.config[server.id]["join"] is True:
            self.config[server.id]["join"] = False
            dataIO.save_json(self.config_file, self.config)
            await self.bot.say("join messages disabled.")

    @welcomer.command(pass_context=True)
    async def disable(self, ctx):
        """Disables the welcomer."""
        server = ctx.message.server
        if server.id not in self.config:
            await self.bot.say("Welcomer was never enabled on this server. :face_palm::drool:")
            return
        del self.config[server.id]
        dataIO.save_json(self.config_file, self.config)
        await self.bot.say("Successfully deleted all settings for welcomer for this server.")

    async def send_welcome(self, server: discord.Server, member: discord.Member,
                           invite: discord.Invite = discord.Invite()):
        message = self.config[server.id]['joinmessage']
        channel = self.config[server.id]["Channel"]
        if self.config[server.id]["Embed"]:
            data = discord.Embed(title="ID: {}".format(member.id),
                                 description=message.format(member, invite, server),
                                 colour=discord.Colour(value=randint(0, 0xFFFFFF)))
            data.set_thumbnail(url=member.avatar_url)
            await self.bot.send_message(server.get_channel(channel), embed=data)
        else:
            await self.bot.send_message(server.get_channel(channel), message.format(member, invite, server))

    async def on_member_join(self, member):
        server = member.server
        if server.id not in self.config:
            return
        if member.bot:
            if self.config[server.id]['botroletoggle'] is True:
                roleobj = discord.utils.get(server.roles, id=self.config[server.id]['botrole'])
                if roleobj is not None:
                    await asyncio.sleep(3)
                    await self.bot.add_roles(member, roleobj)
            return
        await asyncio.sleep(1)
        if self.config[server.id]['join'] is False:
            return
        json_list = self.config[server.id]["Invites"]
        inv_list = await self.bot.invites_from(server)
        invite_available = False
        for a in inv_list:
            try:
                if int(a.uses) > int(json_list[a.url]):
                    await self.send_welcome(server, member, a)
                    invite_available = True
                    break
            except KeyError:
                await self.send_welcome(server, member, a)
                invite_available = True
                break
        if not invite_available:
            a = discord.Invite()
            await self.send_welcome(server, member, a)
        invlist = await self.bot.invites_from(server)
        self.config[server.id]["Invites"] = {}
        for i in invlist:
            self.config[server.id]["Invites"][i.url] = i.uses
        dataIO.save_json(self.config_file, self.config)

    async def on_member_remove(self, member):
        server = member.server
        if server.id not in self.config:
            return
        if self.config[server.id]['leave'] is False:
            return
        message = self.config[server.id]['leavemessage']
        channel = self.config[server.id]["Channel"]
        if self.config[server.id]["Embed"]:
            color = randint(0, 0xFFFFFF)
            data = discord.Embed(title="Member Left!".format(member.id),
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
    if not dataIO.is_valid_json(f):
        print('Creating default settings.json...')
        dataIO.save_json(f, {})


def setup(bot):
    check_folder()
    check_file()
    n = Welcomer(bot)
    bot.add_cog(n)
