import discord

from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    def probability_series(self, p: float, n: int):
        return 1 - (1 - p)**n

    def slovins_equation(self, N: int, e: float):
        return N / (1 + (N * (e**2)))

    @commands.command()
    async def calc(self, ctx, *, arg: str):
        output = None
        output = eval(arg)
        if output is None:
            await ctx.send("Invalid expression")
        else:
            await ctx.send(output)

    @commands.command()
    async def sprob(self, ctx, p: float, n: int = 1):
        desc = 'The probablity of a {:.0f}% chance event occuring at least once in {} attempts'.format(p * 100, n)
        chance = self.probability_series(p, n) * 100
        i = 0
        chance99 = 0.0
        while chance99 <= 99:
            i = i + 1
            chance99 = self.probability_series(p, i) * 100
        embed = discord.Embed(description=desc)
        embed.set_author(name='Series Probability', icon_url=str(self.client.user.avatar_url))
        embed.add_field(name='Probablity', value='{:.3f}%'.format(chance), inline=False)
        embed.add_field(name='Almost guaranteed in (99%): ', value='Attempt %s' % i, inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['slovins'])
    async def slovin(self, ctx, n: int, e: float):
        desc = 'Slovin''s formula is used to determine the sample size given the population size and margin of error'
        embed = discord.Embed(description=desc)
        embed.set_author(name='Determing Sample Size', icon_url=str(self.client.user.avatar_url))
        embed.add_field(name='Population size', value=n, inline=False)
        embed.add_field(name='Error tolerance level', value=e, inline=False)
        embed.add_field(name='Sample size', value='{:.0f}'.format(self.slovins_equation(n, e)), inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Math(client))
    print('math module loaded')
