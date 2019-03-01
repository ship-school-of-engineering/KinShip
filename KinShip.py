import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import find
import platform
import logging

import os
import csv
import configparser
import re
from random import randint

logging.basicConfig(level=logging.INFO)
client = Bot(description="KinShip! - For Ship, By Ship, With Love.", command_prefix="!", pm_help=True)

# Set up configuration
token = 'Error'
is_production = False
try:
    is_production = os.environ['IS_PRODUCTION']
except KeyError:
    print('Environment Variable "IS_PRODUCTION" wasn\'t found! Using config file instead.')
if is_production:
    token = os.environ['TOKEN']
else:
    settings = configparser.RawConfigParser()
    settings.read('config.cfg')
    token = settings.get('Settings', 'token')

# This is what happens everytime the bot launches. In this case, it prints information
# like server count, user count the bot is connected to, and the bot id in the console.
# Additionally, calls setup functions
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
    len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
                                                                               platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    await client.change_presence(game=discord.Game(name="Being neat."))

# Send a welcome message with rules/instructions to new members when they join the server.
# This is not a command. Should be called when the bot sees the event of a member joining.
async def welcome():
    pass

###################
## USER COMMANDS ##
###################

# Basic example of a command to make sure the bot is working.
@client.command(hidden=True)
async def ping():
    await client.say(":thumbsup: Yep, I'm awake!")

# Assign course role
@client.command()
async def enroll(course=None):
    pass

# Assign crew roll
@client.command
async def crew():
    pass

client.run(token)
