#!/usr/bin/env python3

import discord
import asyncio
import os

from utils.secret import key
from utils.utils import async_concurrent, setup
from utils.issue-tracker import create_issue


# Global vars
name = "The All Seeing"
game = "a stupid DND"
client = discord.Client()


"""
on_ready is a function that get's called, when the client has logged in and is ready. Then it set's
up the client by chaning the name and changing the current "game". At the end it starts all the
functions that have to run concurrent.

Doesn't take any parameters
"""
@client.event
async def on_ready():
    # Run the setup function
    await setup(client, name, game)


"""
on_message is a function that will be used to handle commands.

Takes the current message as a parameter
"""
@client.event
async def on_message(message):
    # Make sure we only react on public channels
    if not message.channel.is_private:
        # Make sure the message is addressed to us and not from a bot as per discord TOS
        if client.user in message.mentions and not message.author.bot:
            m = " ".join(message.content.split()[1:])

            if len(m) >= 1:
                if m.split()[0] in ["suggestion", "issue"]:
                    await create_issue(client, message.chanenl, m, message.author.name)

client.run(key)
