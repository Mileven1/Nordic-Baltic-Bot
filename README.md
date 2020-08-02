# Nordic + Baltic BTE Bot

## About

Nordic + Baltic bot is a python built bot, that was mainly designed for the Built Team! If you would like to join the build team use this link! [Here](https://discord.gg/euuq7ae)    

## Commands

Use =help to learn more!

### Basic Commands
=ping
=help
=about
=aboutbot

#### ping

The ping command returns bot response time  
Usage: `=ping`

#### How to create a poll:

Use =poll to start a poll!
##### poll

Creates a poll by adding 👍 and 👎 reactions  
Usage: `=poll [Poll about]`

## Self-Hosting

Self-hosting your own instance of Nordic + Baltic is very easy you just have to dowload the repo and add your token.
  
### Prerequisites

- [Python](https://www.python.org/downloads/) (with pip, so install the latest version)

- [discord.py rewrite branch](https://pypi.org/project/discord.py-rw/) (can be installed via terminal/powershell/cmd window with pip; just enter `pip install discord.py-rw`)

### Installing Files and Configuring Bot

Locate the green "Clone or download" button near the top of this repository. Click that button, then "Download ZIP"  
When the ZIP file downloads, open `config.py` in a text editor and replace the variables as follows;

- config_prefix - The prefix that you want to use to call the bot; ex. if I'm executing the ping command by typing `!ping` the prefix is `!`

- config_description - Your bot's description. This will be displayed in the help command.

- config_owner_id - Your (or the bot owner's) user ID. You can retrieve the ID by enabling [developer mode](https://discordia.me/developer-mode)   and right-clicking on your avatar, then "Copy ID"

- config_bot_log_channel - The ID of the channel you want to send bot logging messages to (cog loading, bot logon, etc.)

- config_command_log_channel -  The ID of the channel you want to send logs for command usage to

- config_error_log_channel - The ID of the channel you want to send logs for errors in commands and other aspects to

- config_guild_log_channel - The ID of the channel you want to send logs for the bot joining/leaving guilds to

Save the config file.

You'll need to replace another important variable. Locate the `bot.py` file and enter a bot token in the quotations after the `token =`, located near the top of the code. To get your bot's token, go to [Discord Developer Portal](https://discordapp.com/developers/applications/me), click "Create Application", give your application a name (the name of your bot), navigate to the Bot section and click "Add Bot" then "Yes, do it!" Then under the title "TOKEN" click "Copy" and paste that value in the token variable.

Then, open terminal/powershell in the bot's folder (navigate to the folder --> shift+right-click) and run the bot.py file with `python bot.py`  
The bot should be up and running!
  
If you're having issues with self-hosting we can sadly not help you with that!

## Contributing

### Source Code Contributions

You can contribute to the project by making a pull request. I'll only merge bug fixes and minor tweaks to the source code, no major command or feature amendments will be merged.


## Copy Right Notice

You can not sell or make a profit out of this bot! This is a open sourced bot made for our Build Team.

### Contributors

There are currently not going to be any contributers at this point of time!
