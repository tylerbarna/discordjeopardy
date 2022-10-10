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
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)