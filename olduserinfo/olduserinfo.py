from discord.ext import commands
import discord
class olduserinfo:
    def __init__(self, bot):
        self.bot = bot

    def fetch_joined_at(self, user, server):
        """Just a special case for someone special :^)"""
        if user.id == "96130341705637888" and server.id == "133049272517001216":
            return datetime.datetime(2016, 1, 10, 6, 8, 4, 443000)
        else:
            return user.joined_at
    @commands.command(pass_context=True, no_pm=True)
    async def olduserinfo(self, ctx, user : discord.Member = None):
        """Shows users's informations"""
        author = ctx.message.author
        server = ctx.message.server
        if not user:
            user = author
        roles = [x.name for x in user.roles if x.name != "@everyone"]
        if not roles: roles = ["None"]
        data = "```python\n"
        data += "Name: {}\n".format(str(user))
        data += "Nickname: {}\n".format(str(user.nick))
        data += "ID: {}\n".format(user.id)
        if user.game is None:
            pass
        elif user.game.url is None:
            data += "Playing: {}\n".format(str(user.game))
        else:
            data += "Streaming: {} ({})\n".format(str(user.game),(user.game.url))
        passed = (ctx.message.timestamp - user.created_at).days
        data += "Created: {} ({} days ago)\n".format(user.created_at, passed)
        joined_at = self.fetch_joined_at(user, server)
        passed = (ctx.message.timestamp - joined_at).days
        data += "Joined: {} ({} days ago)\n".format(joined_at, passed)
        data += "Roles: {}\n".format(", ".join(roles))
        if user.avatar_url != "":
            data += "Avatar:"
            data += "```"
            data += user.avatar_url
        else:
            data += "```"
        await self.bot.say(data)

def setup(bot):
    bot.add_cog(olduserinfo(bot))
