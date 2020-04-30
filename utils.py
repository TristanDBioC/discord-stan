
def welcome(ctx):
	message = '''
	__**{}**__

	**Welcome to the server**
	This is a hangout server created by **{}**.
	This server does not represent any organization or group.
	There are several bots on the server that has different functions.
	You may invite your friends.
	Type __*.invite*__ for the invite link.

	__**Server Bots**__
	**{{Stan}}**
	• Is the overseer, he is created by BioChem to moderate and look after the server in his behalf

	**{{CatBot}}**
	• Monster Hunter World help bot. For more information type __*+help*__

	**{{Groovy}}**
	• Music bot. Join any voice channel then type *-play <title of song>*. __*-help*__ for more info

	**{{Patchbot}}**
	• This bot is responsible for alerting the server for any updates on various games.

	__**Rules**__
	1. **No spamming**
	• Do not send repititive messages that will disrupt others' user experience
	• This includes, but not limited to: messages, files, commands.

	2. **Restrict your bot commands to the appropriate text channel**
	• All bot commands must be done in the channel
	• Although you can activate in any other channel, they bot responses will automatically be deleted.

	3. **Authoritarian Rule**
	• The Emperor has the last say in anything.
	• He may enforce punishment, kicks or bans, without grounds (though unlikely).


	*After reading the server rules,*
	:point_down: *click this to proceed*

	'''.format(ctx.message.guild, ctx.message.author.display_name)
	return message