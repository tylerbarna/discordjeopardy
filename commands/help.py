from discord.ext import commands
import constants

## create help command
class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=constants.helpAliases)
    async def help(self, ctx):
        jeopardyCommands = []
        