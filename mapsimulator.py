import discord, random, time
from discord.ext import commands

gamestatus = discord.Game('A Map Simulation')



class MapMode(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.ismap = False
        self.floor = 0
        self.isgambling = False
        self.gamblechance = 10
        self.gamblecount = 1
        self.gambleValue = 1
        self.gamblePrev = 0
        self.doorroute = [0,0,0,0,0,0] 
        self.lpdoor = False
        self.rpdoor = False
        self.pdoorchance = 10
        self.debug = False
        
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
    async def left(self, ctx):
        """ Picks the door on the left"""
        if self.isgambling == False:
            await ctx.send('You picked the door on the left! Will it open?...')
            if self.doorroute[self.floor] == 0:
                await ctx.send(file=discord.File('Success.gif'))
                self.floor += 1
                self.lpdoor = False
                time.sleep(5)
                await ctx.send('Success! You and your party move to the next chamber!')
                gambleCheck = random.randint(1,100)
                if gambleCheck <= self.gamblechance:
                    await ctx.send('Upon defeating the enemies and soon as you touch the chest, 2 cards appear. Its time to play Higher and Lower!')
                    self.gamblechance = 10
                    time.sleep(2)
                    self.isgambling = True
                    self.gambleValue = random.randint(1,10)
                    self.gamblePrev = random.randint(1,10)
                    while self.gamblePrev == self.gambleValue:
                        self.gamblePrev = random.randint(1,10)
                    await ctx.send('The shown card is a {0}. Do you wish to pick Higher, or Lower?'.format(self.gamblePrev))
            elif self.doorroute[self.floor] == 1:
                await ctx.send(file=discord.File('Failure.gif'))
                time.sleep(5)
                await ctx.send('Failure! You and your party have been kicked from the dungeon! GAME OVER!')
                self.ismap = False
                self.floor = 0
                self.isgambling = False
                self.pdoorchance = 10
                self.gamblechance = 10
                self.lpdoor = False
                self.rpdoor = False
                self.doorroute = [0,0,0,0,0,0]
                await self.bot.change_presence(status=discord.Status.online)
            if self.floor == 6 and self.isgambling == False:
                await ctx.send('Congratulations, You and your party have made it to the 7th Chamber!')
                self.ismap = False
                self.floor = 0
                self.isgambling = False
                self.pdoorchance = 10
                self.gamblechance = 10
                self.lpdoor = False
                self.rpdoor = False
                self.doorroute = [0,0,0,0,0,0]
                await self.bot.change_presence(status=discord.Status.online)
            elif self.floor >0 and self.isgambling == False:
                await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                pdoorrandom = random.randint(1, 100)
                if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                    self.pdoorchance = 10
                    if self.doorroute[self.floor] == 0:
                        self.lpdoor = True
                        await ctx.send('The door on the left begins to glow brightly after you defeated the enemies.')
                    elif self.doorroute[self.floor] == 1:
                        self.rpdoor = True
                        await ctx.send('The door on the right begins to glow brightly after you defeated the enemies.')
        elif self.isgambling == True:
            await ctx.send('A chest is currently being gambled on, so no opening doors for now...')
    
    @commands.command()    
    async def right(self, ctx):
        """Picks the door on the right"""
        if self.isgambling == False:
            await ctx.send('You picked the door on the right! Will it open?...')
            if self.doorroute[self.floor] == 1:
                await ctx.send(file=discord.File('Success.gif'))
                self.floor += 1
                self.rpdoor = False
                time.sleep(5)
                await ctx.send('Success! You and your party move to the next chamber!')
                gambleCheck = random.randint(1,100)
                if gambleCheck <= self.gamblechance:
                    await ctx.send('Upon defeating the enemies and soon as you touch the chest, 2 cards appear. Its time to play Higher and Lower!')
                    self.gamblechance = 10
                    time.sleep(2)
                    self.isgambling = True
                    self.gambleValue = random.randint(1,10)
                    self.gamblePrev = random.randint(1,10)
                    while self.gamblePrev == self.gambleValue:
                        self.gamblePrev = random.randint(1,10)
                    await ctx.send('The shown card is a {0}. Do you wish to pick Higher, or Lower?'.format(self.gamblePrev))
            elif self.doorroute[self.floor] == 0:
                await ctx.send(file=discord.File('Failure.gif'))
                time.sleep(5)
                await ctx.send('Failure! You and your party have been kicked from the dungeon! GAME OVER!')
                self.ismap = False
                self.floor = 0
                self.isgambling = False
                self.pdoorchance = 10
                self.gamblechance = 10
                self.lpdoor = False
                self.rpdoor = False
                self.doorroute = [0,0,0,0,0,0]
                await self.bot.change_presence(status=discord.Status.online)
            if self.floor == 6 and self.isgambling == False:
                await ctx.send('Congratulations, You and your party have made it to the 7th Chamber!')
                self.ismap = False
                self.floor = 0
                self.isgambling = False
                self.pdoorchance = 10
                self.gamblechance = 10
                self.lpdoor = False
                self.rpdoor = False
                self.doorroute = [0,0,0,0,0,0]
                await self.bot.change_presence(status=discord.Status.online)
            elif self.floor >0 and self.isgambling == False:
                await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                pdoorrandom = random.randint(1, 100)
                if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                    self.pdoorchance = 10
                    temp = random.randint(0,1)
                    if self.doorroute[self.floor] == 0:
                        self.lpdoor = True
                        await ctx.send('The door on the left begins to glow brightly after you defeated the enemies.')
                    elif self.doorroute[self.floor] == 1:
                        self.rpdoor = True
                        await ctx.send('The door on the right begins to glow brightly after you defeated the enemies.')
        elif self.isgambling == True:
            await ctx.send('A chest is currently being gambled on, so no opening doors for now...')

    @commands.command()
    async def higher(self, ctx):
        """When Gambling, guess higher"""
        if self.isgambling == True:
            await ctx.send('You picked Higher. The 2nd card spins around, and reveals a...')
            time.sleep(random.randint(1,5))
            await ctx.send('{0}!'.format(self.gambleValue))
            time.sleep(2)
            if self.gambleValue > self.gamblePrev:
                self.gamblecount += 1
                if self.gamblecount <= 4:
                    await ctx.send('Correct! The chest now has x{0} of the original loot! However, another card has shown up!'.format(self.gamblecount))
                    self.gamblePrev = self.gambleValue
                    self.gambleValue = random.randint(1,10)
                    while self.gambleValue == self.gamblePrev:
                        self.gambleValue = random.randint(1,10)
                    await ctx.send('The shown card is now a {0}. Do you wish to pick Higher, or Lower?'.format(self.gamblePrev))
                elif self.gamblecount == 5:
                    await ctx.send('Correct! The chest now has x{0} of the original loot, and has opened up!'.format(self.gamblecount))
                    self.isgambling = False
                    self.gamblecount = 1
                    if self.floor == 6:
                        await ctx.send('You are in the final chamber too! Brilliant way to end it!')
                        self.ismap = False
                        self.floor = 0
                        self.isgambling = False
                        self.pdoorchance = 10
                        self.gamblechance = 10
                        self.lpdoor = False
                        self.rpdoor = False
                        self.doorroute = [0,0,0,0,0,0]
                        await self.bot.change_presence(status=discord.Status.online)
                    elif self.floor <= 5:
                        await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                        pdoorrandom = random.randint(1, 100)
                        if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                            self.pdoorchance = 10
                            if self.doorroute[self.floor] == 0:
                                self.lpdoor = True
                                await ctx.send('The door on the left begins to glow brightly after you stopped gambling.')
                            elif self.doorroute[self.floor] == 1:
                                self.rpdoor = True
                                await ctx.send('The door on the right begins to glow brightly after you stopped gambling.')
            elif self.gambleValue < self.gamblePrev:
                await ctx.send('Incorrect! The chest now remains forever locked. You might as well move onto the next chamber...')
                self.isgambling = False
                self.gamblecount = 1
                if self.floor == 6:
                    await ctx.send('But wait, this is the last chamber. Sad way to end it...')
                    self.ismap = False
                    self.floor = 0
                    self.isgambling = False
                    self.pdoorchance = 10
                    self.gamblechance = 10
                    self.lpdoor = False
                    self.rpdoor = False
                    self.doorroute = [0,0,0,0,0,0]
                    await self.bot.change_presence(status=discord.Status.online)
                elif self.floor <= 5:    
                    await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                    pdoorrandom = random.randint(1, 100)
                    if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                        self.pdoorchance = 10
                        if self.doorroute[self.floor] == 0:
                            self.lpdoor = True
                            await ctx.send('The door on the left begins to glow brightly after you stopped gambling.')
                        elif self.doorroute[self.floor] == 1:
                            self.rpdoor = True
                            await ctx.send('The door on the right begins to glow brightly after you stopped gambling.')
        elif self.isgambling == False:
            await ctx.send('There is no chest that requires gambling...')
    
    @commands.command()
    async def lower(self, ctx):
        """When Gambling, guess lower"""
        if self.isgambling == True:
            await ctx.send('You picked Lower. The 2nd card spins around, and reveals a...')
            time.sleep(random.randint(1,5))
            await ctx.send('{0}!'.format(self.gambleValue))
            time.sleep(2)
            if self.gambleValue < self.gamblePrev:
                self.gamblecount += 1
                if self.gamblecount <= 4:
                    await ctx.send('Correct! The chest now has x{0} of the original loot! However, another card has shown up!'.format(self.gamblecount))
                    self.gamblePrev = self.gambleValue
                    self.gambleValue = random.randint(1,10)
                    while self.gambleValue == self.gamblePrev:
                        self.gambleValue = random.randint(1,10)
                    await ctx.send('The shown card is now a {0}. Do you wish to pick Higher, or Lower?'.format(self.gamblePrev))
                elif self.gamblecount == 5:
                    await ctx.send('Correct! The chest now has x{0} of the original loot, and has opened up!'.format(self.gamblecount))
                    self.isgambling = False
                    self.gamblecount = 1
                    if self.floor == 6:
                        await ctx.send('You are in the final chamber too! Brilliant way to end it!')
                        self.ismap = False
                        self.floor = 0
                        self.isgambling = False
                        self.pdoorchance = 10
                        self.gamblechance = 10
                        self.lpdoor = False
                        self.rpdoor = False
                        self.doorroute = [0,0,0,0,0,0]
                        await self.bot.change_presence(status=discord.Status.online)
                    elif self.floor <= 5:
                        await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                        pdoorrandom = random.randint(1, 100)
                        if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                            self.pdoorchance = 10
                            if self.doorroute[self.floor] == 0:
                                self.lpdoor = True
                                await ctx.send('The door on the left begins to glow brightly after you stopped gambling.')
                            elif self.doorroute[self.floor] == 1:
                                self.rpdoor = True
                                await ctx.send('The door on the right begins to glow brightly after you stopped gambling.')
            elif self.gambleValue > self.gamblePrev:
                await ctx.send('Incorrect! The chest now remains forever locked. You might as well move onto the next chamber...')
                self.isgambling = False
                self.gamblecount = 1
                if self.floor == 6:
                    await ctx.send('But wait, this is the last chamber. Sad way to end it...')
                    self.ismap = False
                    self.floor = 0
                    self.isgambling = False
                    self.pdoorchance = 10
                    self.gamblechance = 10
                    self.lpdoor = False
                    self.rpdoor = False
                    self.doorroute = [0,0,0,0,0,0]
                    await self.bot.change_presence(status=discord.Status.online)
                elif self.floor <= 5:    
                    await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                    pdoorrandom = random.randint(1, 100)
                    if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                        self.pdoorchance = 10
                        if self.doorroute[self.floor] == 0:
                            self.lpdoor = True
                            await ctx.send('The door on the left begins to glow brightly after you stopped gambling.')
                        elif self.doorroute[self.floor] == 1:
                            self.rpdoor = True
                            await ctx.send('The door on the right begins to glow brightly after you stopped gambling.')
        elif self.isgambling == False:
            await ctx.send('There is no chest that requires gambling...')
      
    @commands.command()
    async def stopGamble(self, ctx):
        if self.isgambling == True:
            await ctx.send('You have decided to stop gambling, and your loot multiplier was x{0}.'.format(self.gamblecount))
            self.isgambling = False
            self.gamblecount = 1
            if self.floor == 6:
                await ctx.send('This is the final chamber. Congratulations on getting to the end!')
                self.ismap = False
                self.floor = 0
                self.isgambling = False
                self.pdoorchance = 10
                self.gamblechance = 10
                self.lpdoor = False
                self.rpdoor = False
                self.doorroute = [0,0,0,0,0,0]
                await self.bot.change_presence(status=discord.Status.online)
            elif self.floor <= 5:
                await ctx.send('You and your party are now in Chamber {0}.  Do you want to pick the door on the left or the right?'.format(self.floor+1))
                pdoorrandom = random.randint(1, 100)
                if pdoorrandom <= self.pdoorchance and self.floor <= 4:
                    self.pdoorchance = 10
                    if self.doorroute[self.floor] == 0:
                        self.lpdoor = True
                        await ctx.send('The door on the left begins to glow brightly after you stopped gambling.')
                    elif self.doorroute[self.floor] == 1:
                        self.rpdoor = True
                        await ctx.send('The door on the right begins to glow brightly after you stopped gambling.')
        elif self.isgambling == False:
            await ctx.send('There is no chest that requires gambling...')

    @commands.command()
    async def stopMap(self, ctx):
        """Stops the current Map"""
        await ctx.send('Current Map has been stopped')    
        self.ismap = False
        self.floor = 0
        self.isgambling = False
        self.pdoorchance = 10
        self.gamblechance = 10
        self.lpdoor = False
        self.rpdoor = False
        self.doorroute = [0,0,0,0,0,0]
        await self.bot.change_presence(status=discord.Status.online)
    
    @commands.command()
    async def debugoutput(self, ctx):
        """output class variables"""
        if self.debug == True or str(ctx.message.author) == "Etheren#6893":
            await ctx.send('ismap is currently {0}'.format(self.ismap))
            await ctx.send('you are on floor {0}'.format(self.floor + 1))
        elif self.debug == False:
            await ctx.send('Debugging is not enabled, nor you are my creator.')
        
    @commands.command()
    async def debugDoors(self, ctx):
        """Show the Door Direction Array"""
        if self.debug == True  or str(ctx.message.author) == "Etheren#6893":
            await ctx.send(self.doorroute)
        elif self.debug == False:
            await ctx.send('Debugging is not enabled, nor you are my creator.')
            
    @commands.command()
    async def procParty(self,ctx):
        """Guarantee the next chamber has a Party Door"""
        if self.debug == True  or str(ctx.message.author) == "Etheren#6893":
            self.pdoorchance = 100
            await ctx.send('A Party door is now guaranteed to spawn in the next chamber')
        elif self.debug == False:
            await ctx.send('Debugging is not enabled, nor you are my creator.')

    @commands.command()
    async def procGamble(self,ctx):
        """Guarantee the next chest gives a gamble opportunity"""
        if self.debug == True  or str(ctx.message.author) == "Etheren#6893":
            self.gamblechance = 100
            await ctx.send('The next chest will guarantee a gamble minigame')
        elif self.debug == False:
            await ctx.send('Debugging is not enabled, nor you are my creator.')
            
    @commands.command()
    async def gambleDebug(self,ctx):
        """output debug info relating to High/Low"""
        if self.debug == True  or str(ctx.message.author) == "Etheren#6893":
            await ctx.send('isgambling is currently {0}'.format(self.isgambling))
            await ctx.send('gamblechance is currently {0}'.format(self.gamblechance))
            await ctx.send('gamblecount is currently {0}'.format(self.gamblecount))
            await ctx.send('current number to guess is {0}'.format(self.gambleValue))
            await ctx.send('previous value was {0}'.format(self.gamblePrev))
        elif self.debug == False:
            await ctx.send('Debugging is not enabled, nor you are my creator.')
    
    @commands.command()
    async def partyDebug(self,ctx):
        """output debug info relating to the party door"""
        if self.debug == True or str(ctx.message.author) == "Etheren#6893":
            await ctx.send('Left Party Door is currently {0}'.format(self.lpdoor))
            await ctx.send('Right Party Door is currently {0}'.format(self.rpdoor))
            await ctx.send('pdoor chance is {0}'.format(self.pdoorchance))  
        elif self.debug == False:
            await ctx.send('Debugging is not enabled, nor you are my creator.')
        
    @commands.command()
    async def toggleDebug(self,ctx):
        """Toggle Debugging"""
        if str(ctx.message.author) == "Etheren#6893":
            if self.debug == False:
                self.debug = True
                await ctx.send('Debugging Enabled.')
            elif self.debug == True:
                self.debug = False
                await ctx.send('Debugging Disabled.')
        else:
            await ctx.send('You do not have permission to toggle that.')
            
def setup(bot):
	bot.add_cog(MapMode(bot))