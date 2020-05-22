# discord-stan
Source code for personal discord bot

Version 1.2.1 | May 22, 2020

## Commands
### Prefix = "." (default)
- **invite** - shows invite link
- **ping** - sends out a simple ping
- **clear** - clears the text_channel of a number of messages
- **kick** - kicks the mentioned member
	*needs kick_member permission*
- **ban** - bans the mentioned member
	*needs kick_member permission*
- **addrole** - adds a role to a mentioned discord member
	*needs manage_roles permission*
- **rmrole** - removes a role from a mentioned discord member
	*needs manage_roles permission*
- **change_roles** - changes the role of a mentioned discord member
	*needs manage_roles permission*
- **nickname** - changes the user's nickname
- **weather** - gets the current realtime weather of the specified city

### Owner commands
- **status** - sets bot's status display
- **greet** - sends the welcome message
- **source** - sends the source code of the bot
- **kill** - shuts the bot down
- **load** - loads an extension
- **unload** - unloads an extension


## Events
- on_ready = prints message to console, changes status to version number
- on_raw_reaction_add = allows complete entry to server after reacting to the welcome message
- on_member_join = restricts member visibilty and actions; adds roles
- on_member_remove = sends a message to a certain channel when someone leaves the server
- on_message = checks if bots are messaging in the right channel
- on_command = the bot reacts to valid commands


## Files
- **requirements.txt** - list of dependencies
- **main.py** - core script
- **server_id.json** - contains discord IDs for roles, users, channels, etc. that is used by the bot
- **utils.py** - contains a library of utility functions
- **devs.py** - extension containing dev-only commands
- **events.py** - extension with all event listeners
- **moderation.py** - extension of server management commands
- **misc.py** - miscellaneous commands

## Features
### Gets current weather
- utilizes openweathermap.org api to get the current weather of a city
- shows temperature, precipiation, wind, pressure, and local time
- uses google static map api to display the specified city