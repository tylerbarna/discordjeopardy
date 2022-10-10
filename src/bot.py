## bot.py

import discord
from discord.ext import commands
import os
import sys
import traceback
import asyncio
import json
import random
import time

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)