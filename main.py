import discord
import json

from utils import *
from discord.ext import commands

client = commands.Bot(command_prefix="`")
client.remove_command('help')


''' ~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~ '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

''' if check owner '''
def is_owner(ctx):
    if ctx.message.author.id == get_id("special_users", "owner"):
        return True


''' Get user id from server_id.json '''
def get_id(key1: str, key2: str):
    with open('server_id.json', 'r') as f:
        data = json.load(f)
    return data[key1][key2]


''' ~~~~~~~ Under Development ~~~~~~~~ '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
@client.command()
@commands.has_permissions(is_owner)
async def source(ctx):
    await ctx.send(file=discord.File('main.py'))
    await ctx.send(file=discord.File('utils.py'))
    await ctx.send(file=discord.File('server_id.json'))
    await ctx.send(file=discord.File('requirements.txt'))
    await ctx.send(file=discord.File('readme.md'))


@client.command()
@commands.check(is_owner)
async def prefix(ctx, arg: str):
    client.command_prefix = arg
    await ctx.message.add_reaction("\U00002705")
    await ctx.send("Command prefix changed to {}".format(arg))


@client.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.message.add_reaction("\U00002705")
    

@client.command()
@commands.has_permissions(manage_roles=True)
async def rmrole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.message.add_reaction("\U00002705")


@client.command(aliases=['demote'])
@commands.has_permissions(manage_roles=True)
async def promote(ctx, member: discord.Member, role: discord.Role):
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


''' ~~~~~~~~~~~~~ EVENTS ~~~~~~~~~~~~~~ '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

''' Accepting the server rules '''
@client.event
async def on_raw_reaction_add(payload):
	channel = client.get_channel(payload.channel_id)
	guild = client.get_guild(payload.guild_id)
	user = guild.get_member(payload.user_id)
	rolechk = guild.get_role(get_id("roles","level_zero"))
	if channel != client.get_channel(get_id("channels","setup")):
		return
	if rolechk not in user.roles:
		return
	await user.remove_roles(rolechk)
	await user.add_roles(guild.get_role(get_id("roles","level_one")))
	
	channel = client.get_channel(get_id("channels", "system"))
	await channel.send("{} joined the {}. Welcome! :crossed_swords: :shield:".format(user.mention,guild.name))


''' When the bot script is running and read '''
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
    		name="to your heart	"))
    print("Stan is ready")


''' A member joins the Server'''
''' Assign Roles, added bot naming'''
@client.event
async def on_member_join(member):
    if member.bot == True:
        await member.edit(nick="{{{}}}".format(member.name))
        role = discord.utils.get(member.guild.roles, id=get_id("roles", "senate"))
        await member.add_roles(role)
    else:
    	role = discord.utils.get(member.guild.roles, id=get_id("roles", "level_zero"))
    	await member.add_roles(role)


'''A member leaves the Server'''
@client.event
async def on_member_remove(member):
    channel = client.get_channel(get_id("channels", "system"))
    await channel.send("{} left the empire. Farewell!".format(member))


''' Bot commands are sent in the wrong channel trap'''
@client.event
async def on_message(message):
    if message.author.bot == True and message.author != client.user:
        if message.channel.id not in get_id("channels", "botspam"):
            channel = client.get_channel(697868801697382401)
            await message.delete()
            await message.channel.send("Bots can only send messages in {}".format(channel.mention))
    await client.process_commands(message)


''' ~~~~~~~~~~~~~~~ COMMANDS ~~~~~~~~~~~~~~ '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

''' Invite Link '''
@client.command()
async def invite(ctx):
	await ctx.send("https://discord.gg/gcaHu8G")


''' ping command for the bot'''
@client.command()
async def ping(ctx):
    await ctx.send("{}ms :heart:".format(round(client.latency * 1000)))


''' Clear Messages '''
''' permissions: manage_channel'''
@client.command()
async def clear(ctx, amount:int = 999):
    await ctx.channel.purge(limit=amount)
    await ctx.message.delete()


''' kick members with reason '''
''' permissions: kick_members'''
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


'''ban members with reason'''
'''permissions: ban_members'''
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


''' ~~~~~~~~~~~~~~ OWNER COMMANDS ~~~~~~~~~~~~~~ '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

@client.command()
@commands.check(is_owner)
async def greet(ctx):
	msg = await ctx.send(welcome(ctx))
	await msg.add_reaction("\U00002705")
	await ctx.message.delete()


''' shutdown '''
@client.command()
@commands.check(is_owner)
async def kill(ctx):
    await ctx.send("Stan is logging off")
    exit()


''' load an extension in /cogs folder '''
@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
	client.load_extension("cogs.{}".format(extension))
	await ctx.send("{} loaded".format(extension))


''' unload an extension '''
@client.command()
async def unload(ctx, extension):
	client.unload_extension("cogs.{}".format(extension))
	await ctx.send("{} loaded".format(extension))


''' Create user database '''
client.run("NjkwMDc2NTYyMTEyMjQ5ODU3.Xqm08w.MxcI1TRCZYoVVD8spfsAyruGEnI")
