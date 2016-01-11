# Discordbot3.4

Discordbot3.4 is a testing platform for the current [official unofficial API] from www.discordapp.com.

This project builds on the Python module provided by https://github.com/Rapptz/discord.py/tree/async.

> `discord.py` is an API wrapper for Discord written in Python.

## Plugins

Discordbot3.4 uses the following modules and plugins to work properly:

* [xmltodict] - An XML parser to Python's dictionary, install with `pip install xmltodict`
* [ffmpeg] - For handling multimedia.
* [discord.py] - As mentioned earlier, using the API wrapper provided to use the Discord official unofficial API

## Installation

**Make sure you have the mentioned modules and plugins to continue.**

```sh
$ git clone https://github.com/Palkess/discordbot3.4
$ cd discordbot3.4/config
$ mv preferences.config.example preferences.config
$ nano preferences.config
```
Rename preferences.config.example to preferences.config and replace the values inside to fit your bot's account. 
These settings are only stored locally and are only used to connect the bot with Discord.

Start the bot by running:
```sh
$ cd discordbot3.4
$ python3 main.py
```

## Basic commands

* `!commands` - Prints out all the available commands in `commands.json`
* `!bot` - Info about the bot
* `!play [youtubeID]` - Plays the youtube video in the General-voice channel
* `!stop` - Stops playing the song if its active

Dynamic commands can be found and added in `commands.json`

## //TODO

* Make `!play` into a `!addsong` command instead so we can add multiple songs to a queue
* Rebuild the structure of our json-resources into a consistent model
* Look over the options for a menu so we can access functionality through the terminal

## Links

* Join the discussions over at the Discord API-server through https://discord.gg/0SBTUU1wZTXdsIuk 

## License

See file `LICENSE` in the repo.

[discord.py]: <https://github.com/Rapptz/discord.py/tree/async>
[official unofficial API]: <https://blog.discordapp.com/the-robot-revolution-has-unofficially-begun/>
