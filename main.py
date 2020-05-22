import discord

from discord.ext import commands
from utils import *

client = commands.Bot(command_prefix="`")
client.version = "1.2.1"
client.inv = "https://discord.gg/gcaHu8G"
client.remove_command('help')

client.discord_token = "NjkwMDc2NTYyMTEyMjQ5ODU3.Xqm08w.MxcI1TRCZYoVVD8spfsAyruGEnI"
client.google_mapstatic_key = "AIzaSyBm3HY-1hMy1lZhBdMCHij6MILbXpKFwL8"
client.openweather_key = "92c0a98ba49b179b7de1e9b4c08b0c2f"


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


client.run(client.discord_token)
