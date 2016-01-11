# Discordbot3.4

Discordbot3.4 is a testing platform for the current official unofficial API from www.discordapp.com.

This project builds on the Python module provided by https://github.com/Rapptz/discord.py/tree/async.

> `discord.py` is an API wrapper for Discord written in Python.

### Plugins

Discordbot3.4 uses the follwing modules and plugins to work properly:

* [xmltodict] - An XML parser to Python's dictionary, install with `pip install xmltodict`
* [ffmpeg] - For handling multimedia.
* [discord.py] - As mentioned earlier, using the API wrapper provided to use the Discord official unofficial API

### Installation

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

License
----

See file `LICENSE` in the repo.


Basic commands
----

Under development

[discord.py]: <https://github.com/Rapptz/discord.py/tree/async>

