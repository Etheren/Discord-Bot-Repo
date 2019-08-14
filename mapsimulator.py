import discord, random, time
from discord.ext import commands


gamestatus = discord.Game('A Map Simulation')

debug = True


class MapMode(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.ismap = False
        self.floor = 0
        self.isgambling = False
        self.gamblechance = 10
        self.gambleValue = 1
        self.dooranim = 1
        self.doorroute = [0,0,0,0,0,0]
        
    
    @commands.command()
    async def beginmap(self, ctx):
        """Begin a map Simulation"""
        if self.ismap == False:
            self.ismap = True
            for x in range(6):
                self.doorroute[x] = random.randint(0,1)
            await self.bot.change_presence(status=discord.Status.idle, activity=gamestatus)
            await ctx.send('A Map Sim has been generated! Do you want to pick the door on the left or right?')
        elif self.ismap == True:
            await ctx.send('A Map Sim is already in progress!')
            
    @commands.command()
    async def doorleft(self, ctx):
        """Picks the door on the left"""
        channel = self.bot.get_channel('Put channel ID here')
        await channel.send(file=discord.File('testgif.gif'))
        #add weighting
    
    @commands.command()    
    async def doorright(self, ctx):
        """Picks the door on the right"""
        #add weighting

    @commands.command()
    async def pickhigher(self, ctx):
        """When Gambling, guess higher"""
        #add decision
    
    @commands.command()
    async def picklower(self, ctx):
        """When Gambling, guess lower"""
        #add decision
    
    @commands.command()
    async def debugoutput(self, ctx):
        """output class variables"""
        if debug == True:
            await ctx.send(self.ismap)
            await ctx.send(self.floor)
            await ctx.send(self.isgambling)
            await ctx.send(self.gamblechance)
            await ctx.send(self.gambleValue)
            await ctx.send(self.dooranim)
        elif debug == False:
            await ctx.send('Debugging is not enabled')
        
    @commands.command()
    async def debugDoors(self, ctx):
        """Show the Door Direction Array"""
        if debug == True:
            for x in range(6):
                await ctx.send(self.doorroute[x])
        elif debug == False:
            await ctx.send('Debugging is not enabled')
    
def setup(bot):
	bot.add_cog(MapMode(bot))