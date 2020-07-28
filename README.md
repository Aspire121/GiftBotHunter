# GiftBotHunter

Quick open source code I made for hunting down gift bots. Uses a username filter and an avatar similarity algorithm to a set of images (Psyonix logos) which gift bots often use

Prefix for the bot is `>`

## Setup

For sake of simplicity we will assume you already have a Discord app set up with a bot attached to it in the [Discord dev portal](https://discord.com/developers/) and Python 3.8 installed on your machine.

This requires you to have installed discord.py, imagehash, Pillow and requests

`pip install requests`

`pip install -U Pillow`

`pip install -U discord.py`

`pip install -U imagehash`


- Clone this repository

- Rename utils/keys.example.py to keys.py

- Replace your bot token in keys.py

- Create a passport.json file in the data/scambot_protection folder. Open it and put `{}` as its content. Save.

- Invite the bot to your desired server by using this link `https://discord.com/oauth2/authorize?client_id=<YOUR BOT CLIENT ID GOES HERE>&scope=bot`

- Make a role with "Ban Members" perms and assign it to the bot

- Run the bot using the GiftBotHunter.bat file

## Logging

If you want the bot to log users banned create a channel called `scambot-logs` (make sure the bot has `Read Messages` and `Send Messages` perms to this channel).

## Granting users access

Sometimes the bot might have false positives. To allow a user to join the server use the `>passport @user` command. This will unban the user and grant them access to your server as well as allowing them to bypass the filters.
Use this only if you're sure it's a real user.


