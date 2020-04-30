# discord-stan
Source code for personal discord bot

Version 1.1.4 | April 30, 2020

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
- source = uploads the bot's source files
- status = change bot status
-- change avatar 
-- display 


Events
- on_ready = prints message to console, changes status to version number
- on_raw_reaction_add = allows complete entry to server after reacting to the welcome message
- on_member_join = restricts member visibilty and actions; adds roles
- on_member_remove = sends a message to a certain channel when someone leaves the server
- on_message = checks if bots are messaging in the right channel


Files
- embed.py = a function library
- server_id.json = contains discord IDs for roles, users, channels, etc. that is used by the bot


General
- Followed Pep8 formatting
- Removed comments


Misc. Features
--