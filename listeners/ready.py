import discord
from discord.ext import commands
import asyncio
class ReadyListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has connected to Discord!')
        print(f"Guilds: {len(self.bot.guilds)}")
        print(f"Channels: {len(self.bot.channels)}")
        print(f"Users: {len(self.bot.users)}")
        bit = 0
        notices = [
            '"/help" for commands'
        ]
        await self.bot.change_presence(activity=discord.Game(name=notices[bit]))
        while True:
            bit = (bit + 1) % len(notices)
            await self.bot.change_presence(activity=discord.Game(name=notices[bit]))
            await asyncio.sleep(600)
        