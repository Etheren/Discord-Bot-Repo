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
        self.gamblecount = 1
        self.gambleValue = 1
        self.doorroute = [0,0,0,0,0,0]
        
    def resetMap():
        self.ismap = False
        self.floor = 0
        self.isgambling = False
        self.doorroute = [0,0,0,0,0,0]
        self.bot.change_presence(status=discord.Status.online)
        
    @commands.command()
    async def beginMap(self, ctx):
        """Begin a map Simulation"""
        if self.ismap == False:
            self.ismap = True
            for x in range(6):
                self.doorroute[x] = random.randint(0,1)
            await self.bot.change_presence(status=discord.Status.online, activity=gamestatus)
            await ctx.send('A Map Sim has been generated! You and your party are in Chamber 1. Do you want to pick the door on the left or the right?')
        elif self.ismap == True:
            await ctx.send('A Map Sim is already in progress!')
            
    @commands.command()
    async def doorLeft(self, ctx):
        """ Picks the door on the left"""
        await ctx.send('You picked the door on the left! Will it open?...')
        if self.doorroute[self.floor] == 0:
            await ctx.send(file=discord.File('Success.gif'))
            self.floor += 1
            time.sleep(5)
            await ctx.send('Success! You and your party move to the next chamber!')
        elif self.doorroute[self.floor] == 1:
            await ctx.send(file=discord.File('Failure.gif'))
            time.sleep(5)
            await ctx.send('Failure! You and your party have been kicked from the dungeon!')
            self.ismap = False
            self.floor = 0
            self.isgambling = False
            self.doorroute = [0,0,0,0,0,0]
            await self.bot.change_presence(status=discord.Status.online)
        if self.floor == 6:
            await ctx.send('Congratulations, You and your party have made it to the 7th Chamber!')
            self.ismap = False
            self.floor = 0
            self.isgambling = False
            self.doorroute = [0,0,0,0,0,0]
            await self.bot.change_presence(status=discord.Status.online)
        elif self.floor >0:
            await ctx.send('You and your party are in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))

    @commands.command()    
    async def doorRight(self, ctx):
        """Picks the door on the right"""
        await ctx.send('You picked the door on the right! Will it open?...')
        if self.doorroute[self.floor] == 1:
            await ctx.send(file=discord.File('Success.gif'))
            self.floor += 1
            time.sleep(5)
            await ctx.send('Success! You and your party move to the next chamber!')
        elif self.doorroute[self.floor] == 0:
            await ctx.send(file=discord.File('Failure.gif'))
            time.sleep(5)
            await ctx.send('Failure! You and your party have been kicked from the dungeon!')
            self.ismap = False
            self.floor = 0
            self.isgambling = False
            self.doorroute = [0,0,0,0,0,0]
            await self.bot.change_presence(status=discord.Status.online)
        if self.floor == 6:
            await ctx.send('Congratulations, You and your party have made it to the 7th Chamber!')
            self.ismap = False
            self.floor = 0
            self.isgambling = False
            self.doorroute = [0,0,0,0,0,0]
            await self.bot.change_presence(status=discord.Status.online)
        elif self.floor >0:
            await ctx.send('You and your party are in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
        #add weighting

    @commands.command()
    async def pickHigher(self, ctx):
        """When Gambling, guess higher"""
        await ctx.send('Higher Command')
        #add decision
    
    @commands.command()
    async def pickLower(self, ctx):
        """When Gambling, guess lower"""
        await ctx.send('Lower Command')
        #add decision

    @commands.command()
    async def stopMap(self, ctx):
        """Stops the current Map"""
        await ctx.send('Current Map has been stopped')    
        self.ismap = False
        self.floor = 0
        self.isgambling = False
        self.doorroute = [0,0,0,0,0,0]
        await self.bot.change_presence(status=discord.Status.online)
    
    @commands.command()
    async def debugoutput(self, ctx):
        """output class variables"""
        if debug == True:
            await ctx.send(self.ismap)
            await ctx.send(self.floor)
            await ctx.send(self.isgambling)
            await ctx.send(self.gamblechance)
            await ctx.send(self.gamblecount)
            await ctx.send(self.gambleValue)
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