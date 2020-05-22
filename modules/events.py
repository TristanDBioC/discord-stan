import discord
import os

from discord.ext import commands
from utils import *


class EventHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        version = discord.Game("Version {}".format(self.client.version))
        await self.client.change_presence(activity=version)
        try:
            os.remove('discord-stan.zip')
        except FileNotFoundError:
            pass
        print("Stan is ready")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        guild = self.client.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        rolechk = guild.get_role(utility.get_id("roles", "level_zero"))
        if channel != self.client.get_channel(utility.get_id("channels", "setup")):
            return
        if rolechk not in user.roles:
            return
        await user.remove_roles(rolechk)
        await user.add_roles(guild.get_role(utility.get_id("roles", "level_one")))
        channel = self.client.get_channel(utility.get_id("channels", "system"))
        await channel.send("{} joined the {}. Welcome!{}".format(user.mention, guild.name, discord.utils.get(guild.emojis, name='stan_happy')))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot is True:
            await member.edit(nick="{{{}}}".format(member.name))
            role = discord.utils.get(
                member.guild.roles, id=utility.get_id("roles", "senate"))
            await member.add_roles(role)
        else:
            role = discord.utils.get(
                member.guild.roles, id=utility.get_id("roles", "level_zero"))
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(utility.get_id("channels", "system"))
        await channel.send("{} left the empire. Farewell!{}".format(member, discord.utils.get(member.guild.emojis, name='stan_neutral')))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot is True and message.author != self.client.user:
            if message.channel.id not in utility.get_id("channels", "botspam"):
                channel = self.client.get_channel(697868801697382401)
                await message.delete()
                await message.channel.send("Bots can only send messages in {}".
                                           format(channel.mention))

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='stan_smile')
        await ctx.message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = self.client.get_channel(utility.get_id("channels", "errors"))
        user = ctx.author
        content = ctx.message.content
        await channel.send('In {} by {}\n"{}"\n{}'.format(ctx.channel.mention, user, content[1:], error))
        raise error


def setup(client):
    client.add_cog(EventHandler(client))
    print('events module loaded')
