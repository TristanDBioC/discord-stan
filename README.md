# discord-stan
Source code for personal discord bot

Version 1.1.5 | May 5, 2020

## Commands
### Prefix = "." (default)
- **invite** shows invite link
- **ping** sends out a simple ping
- **clear** clears the text_channel of a number of messages
- **kick** kicks the mentioned member
	*needs kick_member permission*
- **ban** bans the mentioned member
	*needs kick_member permission*
- **addrole** adds a role to a mentioned discord member
	*needs manage_roles permission*
- **rmrole** removes a role from a mentioned discord member
	*needs manage_roles permission*
- **change_roles** changes the role of a mentioned discord member
	*needs manage_roles permission*

### Owner commands
- **status** sets bot's status display
- **greet** sends the welcome message
- **source** sends the source code of the bot
- **load** loads an extension
- **unload** unloads an extension
- **kill** shuts the bot down


## Events
- on_ready = prints message to console, changes status to version number
- on_raw_reaction_add = allows complete entry to server after reacting to the welcome message
- on_member_join = restricts member visibilty and actions; adds roles
- on_member_remove = sends a message to a certain channel when someone leaves the server
- on_message = checks if bots are messaging in the right channel


## Files
- requirements.txt = list of dependencies
- embed.py = a function library
- server_id.json = contains discord IDs for roles, users, channels, etc. that is used by the bot


## Misc. Features
--