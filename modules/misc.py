import discord

from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(self.client.inv)

    @commands.command()
    async def ping(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='stan_happy')
        await ctx.send("{}ms {}".format(round(self.client.latency * 1000), emoji))

    @commands.command(aliases=["nick", "name"])
    async def nickname(self, ctx, *, arg):
        await ctx.author.edit(nick=arg)


def setup(client):
    client.add_cog(Misc(client))
    print("misc module loaded")
