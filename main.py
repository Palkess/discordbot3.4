import discord
import json
import threading
import os
import asyncio
import xmltodict

client = discord.Client()
audioplayer = None

@client.event
@asyncio.coroutine
def on_message(message):
    # Current solution to updating commands during runtime
    f = open("commands.json", "r")
    jsonData = f.read()

    data = json.loads(jsonData)

    messageSplit = message.content.split()

    if message.content.startswith('!commands'):
        msg = "Commands: \n"
        for command,string in data['commands'].items():
            msg += "%s - %s \n" % (command, string)

        yield from client.send_message(message.channel, msg)

    if message.content.startswith('!bot'):
        msg = "My name is %s ! You can find my Open Source code over at https://github.com/Palkess/discordbot3.4 !" % (client.user.name)
        yield from client.send_message(message.channel, msg)

    if message.content.startswith('!play'):
        if "watch" in messageSplit[1] or "v=" in messageSplit[1] or "youtube" in messageSplit[1]:
            yield from client.send_message(message.channel, "Only enter the ID in the link. you can find it after `watch?v=` in the youtube URL")
        else:
            if client.voice == None:
                channel = discord.utils.get(message.server.channels, name='General', type=discord.ChannelType.voice)
                yield from client.join_voice_channel(channel)

            channel = discord.utils.get(message.server.channels, name='General', type=discord.ChannelType.voice)
            voice = client.voice
            global audioplayer
            audioplayer = voice.create_ytdl_player("https://www.youtube.com/watch?v=%s" % (messageSplit[1]))
            yield from client.send_message(message.channel, "Playing https://www.youtube.com/watch?v=%s" % (messageSplit[1]))
            audioplayer.start()

    if message.content.startswith("!stop"):
        global audioplayer
        # If we actually have a player active in our variable, stop it
        if type(audioplayer).__name__=='ProcessPlayer' and audioplayer.is_playing():
            audioplayer.stop()

    if messageSplit[0] in data['commands']:
        if "template" in data['commands'][messageSplit[0]]:
            yield from client.send_message(message.channel, data['commands'][messageSplit[0]]['template'] % (message.author, messageSplit[1]))
        else:
            print(message.channel)
            yield from client.send_message(message.channel, data['commands'][messageSplit[0]])

@client.event
@asyncio.coroutine
def on_member_join(member):
    server = member.server
    yield from client.send_message(server, 'Welcome {0} to {1.name}!'.format(member.mention(), server))

@client.event
@asyncio.coroutine
def on_member_remove(member):
    yield from client.send_message(member.server, '%s disconnected from the server' % (member.name))

@client.event
@asyncio.coroutine
def on_server_join(server):
    yield from client.send_message(server, "Well met citizen of %s ! I'm your humble bot, at your service!" % (server.name))

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

f = open("config/preferences.config", "r")
configString = f.read()

config = xmltodict.parse(configString)

client.run(config['bot']['email'], config['bot']['password'])