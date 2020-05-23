import discord

from discord.ext import commands
from utils import *

client = commands.Bot(command_prefix="`")
client.version = "1.2.2"
client.inv = "https://discord.gg/gcaHu8G"  # invite link
client.remove_command('help')


@client.command()
@commands.check(utility.is_owner)
async def load(ctx, arg):
    client.load_extension('modules.{}'.format(arg))
    emoji = discord.utils.get(ctx.guild.emojis, name='stan_happy')
    await ctx.send('{} module is loaded {}'.format(arg, emoji))


@client.command()
@commands.check(utility.is_owner)
async def unload(ctx, arg):
    if arg == 'devs.py':
        emoji = discord.utils.get(ctx.guild.emojis, name='stan_suspicious')
        await ctx.send('This module cannot be unloaded {}'.format(emoji))
        return
    client.unload_extension('modules.{}'.format(arg))
    emoji = discord.utils.get(ctx.guild.emojis, name='stan_neutral')
    await ctx.send('{} module is unloaded {}'.format(arg, emoji))


@client.command(aliases=['die', 'shutdown', 'sleep'])
@commands.check(utility.is_owner)
async def kill(ctx):
    emoji = discord.utils.get(ctx.guild.emojis, name='stan_neutral')
    await ctx.send('Stan logging off {}'.format(emoji))
    quit()


client.load_extension('modules.devs')
client.load_extension('modules.moderation')
client.load_extension('modules.events')
client.load_extension('modules.misc')
client.load_extension('modules.weather')


client.run(utility.get_api_key("discord"))
