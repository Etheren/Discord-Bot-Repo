import discord, random
from discord.ext import commands

class MapCog(commands.Cog):

    def __init__(self, bot)
    self.bot = bot
    self.floor = 1
    self.isgambling = False
    self.gamblechance = 10
    self.gambleValue = 1
    self.dooranim = 1
    
    @commands.command()
    async def doorleft(self, ctx):
        """Picks the door on the left"""
        #add weighting
        
    async def doorright(self, ctx):
        """Picks the door on the right"""
        #add weighting

    async def pickhigher(self, ctx):
        """When Gambling, guess higher"""
        #add decision
        
    async def picklower(self, ctx):
        """When Gambling, guess lower"""
        #add decision
        