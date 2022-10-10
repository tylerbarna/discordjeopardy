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
## read secrets.json and get token
json_file = open("secrets.json")
TOKEN = json.load(json_file)["token"]

#TOKEN = os.environ.get('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)