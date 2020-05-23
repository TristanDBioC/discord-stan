import discord

from utils import *
from zipfile import ZipFile
from discord.ext import commands


class Devs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def source(self, ctx):
        try:
            with ZipFile('discord-stan.zip', 'x') as f:
                f.write('README.md')
                f.write('main.py')
                f.write('utils.py')
                f.write('api_keys.json')
                f.write('server_id.json')
                f.write('requirements.txt')
                f.write('changelog.txt')
                f.write('modules/devs.py')
                f.write('modules/events.py')
                f.write('modules/moderation.py')
                f.write('modules/misc.py')
                f.write('modules/weather.py')
        except FileExistsError:
            pass
        finally:
            emoji = discord.utils.get(ctx.guild.emojis, name='stan_blush')
            msg = "Here is my source code. Please handle it with care {}".format(emoji)
            await ctx.send(file=discord.File('discord-stan.zip'), content=msg)

    @commands.command()
    @commands.check(utility.is_owner)
    async def status(self, ctx, *, arg='reset'):
        if arg == 'reset':
            version = discord.Game("Version {}".format(self.client.version))
        else:
            version = discord.Game(arg)
        await self.client.change_presence(activity=version)

    @commands.command(aliases=["welcome"])
    @commands.check(utility.is_owner)
    async def greet(self, ctx):
        msg = await ctx.send(utility.welcome(ctx))
        await msg.add_reaction(discord.utils.get(ctx.guild.emojis, name='empire'))
        await ctx.message.delete()

    @commands.command()
    @commands.check(utility.is_owner)
    async def prefix(self, ctx, arg: str):
        self.client.command_prefix = arg
        await ctx.send("Command prefix changed to {}".format(arg))


def setup(client):
    client.add_cog(Devs(client))
    print('devs module loaded')
