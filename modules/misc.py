import discord
import psutil

from discord.ext import commands
from utils import *


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(utility.is_owner)
    async def test(self, ctx):
        await ctx.send(str(discord.ClientUser.avatar_url))

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(constants.inv)

    @commands.command()
    async def ping(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='stan_happy')
        await ctx.send("{}ms {}".format(round(self.client.latency * 1000), emoji))

    @commands.command(aliases=["nick", "name"])
    async def nickname(self, ctx, *, arg):
        await ctx.author.edit(nick=arg)

    @commands.command(aliases=['info'])
    async def stats(self, ctx):
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        guild_count = len(self.client.guilds)
        stat_embed = discord.Embed(title='Bot Information')
        disk_total = psutil.disk_usage('/').total / (1024**3)
        disk_used = psutil.disk_usage('/').used / (1024**3)

        stat_embed.set_author(name='Stan', url=constants.bot_url, icon_url=str(self.client.user.avatar_url))
        stat_embed.add_field(name='Version',
                             value=constants.version)
        stat_embed.add_field(name='CPU-Usage',
                             value='%s %%' % cpu_usage, inline=True)
        stat_embed.add_field(name='Memory Usage',
                             value='%s %%' % memory_usage, inline=True)
        stat_embed.add_field(name='Disk Usage',
                             value='{:.2f}/{:.2f} gb'.format(disk_used, disk_total), inline=True)
        stat_embed.add_field(name='Servers',
                             value=guild_count, inline=True)
        await ctx.send(embed=stat_embed)


def setup(client):
    client.add_cog(Misc(client))
    print("misc module loaded")
