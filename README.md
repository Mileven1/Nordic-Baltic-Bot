# wafflebot

## About

wafflebot is a multifunctional Discord bot written in discord.py. wafflebot is public, but it's reccomended that you host your own instance the bot won't accomodate custom log channels, etc. on the public instance. See section below for self-hosting information. wafflebot is developed by waffles#9298. If you need support with the bot or self-hosting, join the [support server](https://discord.gg/bfJ8UsT)

### Links

[Support Server](https://discord.gg/bfJ8UsT)  
[Invite the Bot to Your Server](https://discordapp.com/api/oauth2/authorize?client_id=582380938667884548&permissions=8&scope=bot)  
[View Bot Documentation Externally](https://ben-waffles.github.io/wafflebot)  

## Commands

[represents optional arguements] (represents required arguements)

### Basic Commands

#### ping

The ping command returns bot response time  
Usage: `-ping`

#### Commands for Creating Polls: poll and mpoll

You can create polls using the bot. Invoking the following commands makes the bot add reactions to the invoking message to allow for east voting

##### poll

Creates a poll by adding 👍 and 👎 reactions  
Usage: `-poll [content/question of poll]`

##### mpoll

Creates a poll by adding 👍, 👎 and 🤷 reactions  
Usage: `-poll [content/question of poll]`

## Self-Hosting

Self-hosting your own instance of wafflebot is very simple first, install the needed Prequisites .
  
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
  
If you're having issues with self-hosting, join the [support server](https://discord.gg/NfrvPfm) for assistance

## Contributing

### Source Code Contributions

You can contribute to the project by making a pull request. I'll only merge bug fixes and minor tweaks to the source code, no major command or feature amendments will be merged.

### Documentation Contributions

Major additions or amendments to the documentation this README file, the HTML version of the documentation, or the wiki will typically be merged if they're sensical and helpful. If you can, reflect any changes to this file on the index.html file in the docs folder on this repository if possible and applicable.

### Contributors

There are no contributors aside from myself at this point in time, but in the event that someone aside from me contributes to the bot's source code or documentation, their and any other contributor's names will be listed here
