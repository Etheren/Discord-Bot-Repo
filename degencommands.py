import discord
from discord.ext import commands

class DegenCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0
    
    @commands.command()
    async def addcounter(self, ctx):
        self.counter += 1
        await ctx.send('Counter is now %d' % self.counter)

def setup(bot):
	bot.add_cog(DegenCog(bot))