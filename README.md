# discord-stan
Source code for personal discord bot

Version 1.00 | April 27, 2020

Commands
- Prefix = "." (default)
- ping = sends out a simple ping
- greet = creates wecelcome message based on embed.py and adds a reaction to it
- kick = kicks a member (kick_members)
- ban = bans a member (ban_members)
- invite = shows the invite link 
- prefix = changes the command_prefix (is_owner)
- addrole = adds role
- rmrole = removes roles
- promote/demote = changes someone's role but only to par with your level
-- upload source files
-- change avatar 
-- change status
-- display 


Events
- on_member_join = restricts member visibilty and actions; adds roles
- on_raw_reaction_add = allows complete entry to server after reacting to the welcome message
- on_message = checks if bots are messaging in the right channel
- on_member_remove = sends a message to a certain channel when someone leaves the server

Files
- embed.py = a function library
- server_id.json = contains discord IDs for roles, users, channels, etc. that is used by the bot

Misc. Features
--