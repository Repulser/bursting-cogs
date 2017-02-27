from discord.ext import commands
from cogs.utils import checks
import datetime
from cogs.utils.dataIO import fileIO
import discord
import asyncio
import os
from random import choice, randint

inv_settings = {"Channel": None, "toggleedit": False, "toggledelete": False, "toggleuser": False, "toggleroles": False,
                "togglevoice": False,
                "toggleban": False}


class invitemirror:
    def __init__(self, bot):
        self.bot = bot
        self.direct = "data/modlogset/settings.json"

    @checks.admin_or_permissions(administrator=True)
    @commands.group(name='modlogtoggle', pass_context=True, no_pm=True)
    async def modlogtoggles(self, ctx):
        """Toggle which server activity to log"""
        if ctx.invoked_subcommand is None:
            db = fileIO(self.direct, "load")
            await self.bot.send_cmd_help(ctx)
            try:
                await self.bot.say("```Current settings:\a\n\a\n" + "Edit: " + str(
                    db[ctx.message.server.id]['toggleedit']) + "\nDelete: " + str(
                    db[ctx.message.server.id]['toggledelete']) + "\nUser: " + str(
                    db[ctx.message.server.id]['toggleuser']) + "\nRoles: " + str(
                    db[ctx.message.server.id]['toggleroles']) + "\nVoice: " + str(
                    db[ctx.message.server.id]['togglevoice']) + "\nBan: " + str(
                    db[ctx.message.server.id]['toggleban']) + "```")
            except KeyError:
                return

    @checks.admin_or_permissions(administrator=True)
    @commands.group(pass_context=True, name='modlogset', no_pm=True)
    async def modlogset(self, ctx):
        """Change modlog settings"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @modlogset.command(pass_context=True, name='channel', no_pm=True)
    async def channel(self, ctx):
        """Set the channel to send notifications to"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if ctx.message.server.me.permissions_in(ctx.message.channel).send_messages:
            if server.id in db:
                db[server.id]['Channel'] = ctx.message.channel.id
                fileIO(self.direct, "save", db)
                await self.bot.say("Channel changed.")
                return
            if not server.id in db:
                db[server.id] = inv_settings
                db[server.id]["Channel"] = ctx.message.channel.id
                fileIO(self.direct, "save", db)
                await self.bot.say("I will now send toggled modlog notifications here")
        else:
            return

    @modlogset.command(name='disable', pass_context=True, no_pm=True)
    async def disable(self, ctx):
        """Disables the modlog"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            await self.bot.say("Server not found, use modlogset to set a channnel")
            return
        del db[server.id]
        fileIO(self.direct, "save", db)
        await self.bot.say("I will no longer send modlog notifications here")

    @modlogtoggles.command(name='edit', pass_context=True, no_pm=True)
    async def edit(self, ctx):
        """Toggle notifications when a member edits their message"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["toggleedit"] == False:
            db[server.id]["toggleedit"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Edit messages enabled")
        elif db[server.id]["toggleedit"] == True:
            db[server.id]["toggleedit"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Edit messages disabled")

    @modlogtoggles.command(name='delete', pass_context=True, no_pm=True)
    async def delete(self, ctx):
        """Toggle notifications when a member delete their message"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["toggledelete"] == False:
            db[server.id]["toggledelete"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Delete messages enabled")
        elif db[server.id]["toggledelete"] == True:
            db[server.id]["toggledelete"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Delete messages disabled")

    @modlogtoggles.command(name='user', pass_context=True, no_pm=True)
    async def user(self, ctx):
        """Toggle notifications when a user changes their profile"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["toggleuser"] == False:
            db[server.id]["toggleuser"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("User messages enabled")
        elif db[server.id]["toggleuser"] == True:
            db[server.id]["toggleuser"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("User messages disabled")

    @modlogtoggles.command(name='roles', pass_context=True, no_pm=True)
    async def roles(self, ctx):
        """Toggle notifications when roles change"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["toggleroles"] == False:
            db[server.id]["toggleroles"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Role messages enabled")
        elif db[server.id]["toggleroles"] == True:
            db[server.id]["toggleroles"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Role messages disabled")

    @modlogtoggles.command(name='voice', pass_context=True, no_pm=True)
    async def voice(self, ctx):
        """Toggle notifications when voice status change"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["togglevoice"] == False:
            db[server.id]["togglevoice"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Voice messages enabled")
        elif db[server.id]["togglevoice"] == True:
            db[server.id]["togglevoice"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Voice messages disabled")

    @modlogtoggles.command(name='ban', pass_context=True, no_pm=True)
    async def ban(self, ctx):
        """Toggle notifications when a user is banned"""
        server = ctx.message.server
        db = fileIO(self.direct, "load")
        if db[server.id]["toggleban"] == False:
            db[server.id]["toggleban"] = True
            fileIO(self.direct, "save", db)
            await self.bot.say("Ban messages enabled")
        elif db[server.id]["toggleban"] == True:
            db[server.id]["toggleban"] = False
            fileIO(self.direct, "save", db)
            await self.bot.say("Ban messages disabled")

    async def on_message_delete(self, message):
        server = message.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if db[server.id]['toggledelete'] == False:
            return
        channel = db[server.id]["Channel"]
        time = datetime.datetime.now()
        fmt = '[ %H:%M:%S ]'
        
        name = message.author
        name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
        delmessage = discord.Embed(description=name, colour=discord.Color.purple())
        infomessage = "A message by __{}__, was deleted in {}".format(message.author.nick if message.author.nick else message.author.name, message.channel.mention)
        delmessage.add_field(name="Info:", value=infomessage, inline=False)
        delmessage.add_field(name="Message:", value=message.content)
        delmessage.set_footer(text="User ID: {}".format(message.author.id))
        delmessage.set_author(name=time.strftime(fmt) + " - Deleted Message", url="http://i.imgur.com/fJpAFgN.png")
        delmessage.set_thumbnail(url="http://i.imgur.com/fJpAFgN.png")

        try:
            await self.bot.send_message(server.get_channel(channel), embed=delmessage)
        except discord.HTTPException:
            await self.bot.send_message(server.get_channel(channel),
                                        "``{}`` {} ({}) Deleted his message in {}:\a\n\a\n ``{}``".format(
                                            time.strftime(fmt), message.author, message.author.id, message.channel,
                                            message.content))

    async def on_message_edit(self, before, after):
        server = before.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if db[server.id]['toggleedit'] == False:
            return
        if before.content == after.content:
            return
        channel = db[server.id]["Channel"]
        time = datetime.datetime.now()
        fmt = '[ %H:%M:%S ]'
        
        name = before.author
        name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
        delmessage = discord.Embed(description=name, colour=discord.Color.green())
        infomessage = "A message by __{}__, was edited in {}".format(before.author.nick if before.author.nick else before.author.name, before.channel.mention)
        delmessage.add_field(name="Info:", value=infomessage, inline=False)
        delmessage.add_field(name="Before Message:", value=before.content, inline=False)
        delmessage.add_field(name="After Message:", value=after.content)
        delmessage.set_footer(text="User ID: {}".format(before.author.id))
        delmessage.set_author(name=time.strftime(fmt) + " - Edited Message", url="http://i.imgur.com/Q8SzUdG.png")
        delmessage.set_thumbnail(url="http://i.imgur.com/Q8SzUdG.png")

        try:
            await self.bot.send_message(server.get_channel(channel), embed=delmessage)
        except discord.HTTPException:        
            await self.bot.send_message(server.get_channel(channel),
                                    "``{}`` {} ({}) Edited his message in {}:\a\n\a\n__**Before:**__ ``{}``\a\n\a\n__**After:**__ ``{}``".format(
                                        time.strftime(fmt), before.author, before.author.id, before.channel,
                                        before.content, after.content))

    async def on_voice_state_update(self, before, after):
        server = before.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if db[server.id]['togglevoice'] == False:
            return
        channel = db[server.id]["Channel"]
        time = datetime.datetime.now()
        fmt = '[ %H:%M:%S ]'
        
        name = before
        name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
        updmessage = discord.Embed(description=name, colour=discord.Color.blue())
        infomessage = "__{}__'s voice status has changed".format(before.name)
        updmessage.add_field(name="Info:", value=infomessage, inline=False)
        updmessage.add_field(name="Voice Channel Before:", value=before.voice_channel)
        updmessage.add_field(name="Voice Channel After:", value=after.voice_channel)
        updmessage.set_footer(text="User ID: {}".format(before.id))
        updmessage.set_author(name=time.strftime(fmt) + " - Voice Channel Changed", url="http://i.imgur.com/8gD34rt.png")
        updmessage.set_thumbnail(url="http://i.imgur.com/8gD34rt.png")

        try:
            await self.bot.send_message(server.get_channel(channel), embed=updmessage)
        except discord.HTTPException:
            await self.bot.send_message(server.get_channel(channel),
                                        "``{}`` {} ({}) Voice status changed:\a\n\a\n__**Before:**__ ``{}``\a\n\a\n__**After:**__ ``{}``".format(
                                            time.strftime(fmt), before, before.id,
                                            before.voice_channel, after.voice_channel))

    async def on_member_update(self, before, after):
        server = before.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if db[server.id]['toggleuser'] and db[server.id]['toggleroles'] == False:
            return
        channel = db[server.id]["Channel"]
        time = datetime.datetime.now()
        fmt = '[ %H:%M:%S ]'
        if not before.nick == after.nick:
            name = before
            name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
            updmessage = discord.Embed(description=name, colour=discord.Color.orange())
            infomessage = "__{}__'s nickname has changed".format(before.name)
            updmessage.add_field(name="Info:", value=infomessage, inline=False)
            updmessage.add_field(name="Nickname Before:", value=before.nick)
            updmessage.add_field(name="Nickname After:", value=after.nick)
            updmessage.set_footer(text="User ID: {}".format(before.id))
            updmessage.set_author(name=time.strftime(fmt) + " - Nickname Changed", url="http://i.imgur.com/I5q71rj.png")
            updmessage.set_thumbnail(url="http://i.imgur.com/I5q71rj.png")

            try:
                await self.bot.send_message(server.get_channel(channel), embed=updmessage)
            except discord.HTTPException: 
                await self.bot.send_message(server.get_channel(channel),
                                            "``{}`` {} ({}) User nickname changed:\a\n\a\n__**Before:**__ ``{}``\a\n\a\n__**After:**__ ``{}``".format(
                                                time.strftime(fmt), before, before.id,
                                                before.nick, after.nick))
        if not before.roles == after.roles:
            name = before
            name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
            updmessage = discord.Embed(description=name, colour=discord.Color.gold())
            infomessage = "__{}__'s roles have changed".format(before.name)
            updmessage.add_field(name="Info:", value=infomessage, inline=False)
            updmessage.add_field(name="Roles Before:", value=", ".join([r.name for r in before.roles if r.name != "@everyone"]), inline=False)
            updmessage.add_field(name="Roles After:", value=", ".join([r.name for r in after.roles if r.name != "@everyone"]))
            updmessage.set_footer(text="User ID: {}".format(before.id))
            updmessage.set_author(name=time.strftime(fmt) + " - Role Changed", url="http://i.imgur.com/QD39cFE.png")
            updmessage.set_thumbnail(url="http://i.imgur.com/QD39cFE.png")

            try:
                await self.bot.send_message(server.get_channel(channel), embed=updmessage)
            except discord.HTTPException:
                await self.bot.send_message(server.get_channel(channel),
                                            "``{}`` {} ({}) User roles changed:\a\n\a\n__**Before:**__ ``{}``\a\n\a\n__**After:**__ ``{}``".format(
                                                time.strftime(fmt), before, before.id,
                                                ",".join([r.name for r in before.roles if r.name != "@everyone"]),
                                                ",".join([r.name for r in after.roles if r.name != "@everyone"])))

    async def on_member_ban(self, member):
        server = member.server
        db = fileIO(self.direct, "load")
        if not server.id in db:
            return
        if db[server.id]['toggleuser'] == False:
            return
        channel = db[server.id]["Channel"]
        time = datetime.datetime.now()
        fmt = '[ %H:%M:%S ]'
        
        name = member
        name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
        banmessage = discord.Embed(description=name, colour=discord.Color.red())
        infomessage = "__{}__ has been banned from the server.".format(member.nick if member.nick else member.name)
        banmessage.add_field(name="Info:", value=infomessage, inline=False)
        banmessage.set_footer(text="User ID: {}".format(member.id))
        banmessage.set_author(name=time.strftime(fmt) + " - Banned User", url="http://i.imgur.com/Imx0Znm.png")
        banmessage.set_thumbnail(url="http://i.imgur.com/Imx0Znm.png")

        try:
            await self.bot.send_message(server.get_channel(channel), embed=banmessage)
        except discord.HTTPException:
            await self.bot.send_message(server.get_channel(channel),
                                        "``{}`` {} ({}) has been __**banned**__".format(
                                            time.strftime(fmt), member, member.id))


def check_folder():
    if not os.path.exists('data/modlogset'):
        print('Creating data/modlogset folder...')
        os.makedirs('data/modlogset')


def check_file():
    f = 'data/modlogset/settings.json'
    if not fileIO(f, 'check'):
        print('Creating default settings.json...')
        fileIO(f, 'save', {})


def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(invitemirror(bot))
