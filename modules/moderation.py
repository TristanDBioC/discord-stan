import discord

from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount: int = 999):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: discord.Member, r):
        role = discord.utils.get(ctx.guild.roles, name=r)
        await member.add_roles(role)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def rmrole(self, ctx, member: discord.Member, r):
        role = discord.utils.get(ctx.guild.roles, name=r)
        await member.remove_roles(role)

    @commands.command(aliases=['demote', 'promote'])
    @commands.has_permissions(manage_roles=True)
    async def change_roles(self, ctx, member: discord.Member, r):
        role = discord.utils.get(ctx.guild.roles, name=r)
        if ctx.author.top_role.position < member.top_role.position:
            await ctx.send("You cannot dictate someone higher than you")
            return
        if ctx.author.top_role.position < role.position:
            await ctx.send("You do not have authority to bestow this rank")
            return
        for x in member.roles:
            if x.position > 0:
                await member.remove_roles(x)
        await member.add_roles(role)


def setup(client):
    client.add_cog(Moderation(client))
    print('moderation module loaded')
