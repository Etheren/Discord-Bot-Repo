import discord, discordtoken , random, time
from discord.ext import commands

TOKEN = discordtoken.TOKENONE
#You're not getting the bot token THIS easily. Ive already seen one server get
#Destroyed by it being left here.

counterCheck = 0

description = '''AmiBot'''
mapToggle = False
voiceToggle = False
bot = commands.Bot(command_prefix=';', description=description)
client = discord.AutoShardedClient()
#bot.load_extension('mapsimulator')
#bot.load_extension('degencommands')

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world!")

@bot.command()
async def add(ctx, left : int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)    
    
@bot.command()
async def randomroll(ctx, left : int, right : int):
    """Roll a random number between 1 and 10"""
    randomoutput = random.randint(left, right)
    await ctx.send(randomoutput)
    
@bot.command()
async def toggleMap(ctx):
    """Enable/Disable Map Mode"""
    global mapToggle
    if mapToggle == False:
        mapToggle = True
        bot.load_extension('mapsimulator')
        await ctx.send('Map Mode Enabled')
    elif mapToggle == True:
        mapToggle = False
        bot.unload_extension('mapsimulator')
        await ctx.send('Map Mode Disabled')

@bot.command()
async def toggleVoice(ctx):
    """Enable/Disable Voice Mode"""
    global voiceToggle
    if voiceToggle == False:
        voiceToggle = True
        bot.load_extension('voicestuff')
        await ctx.send('Voice Enabled')
    elif voiceToggle == True:
        voiceToggle = False
        bot.unload_extension('voicestuff')
        await ctx.send('Voice Disabled')
        
@bot.command()
async def shutdownBot(ctx):
    """Shut the bot down"""
    if str(ctx.message.author) == "Etheren#6893":
        await ctx.send('Shutting the bot down.')
        await bot.close()
    else: 
        await ctx.send('Only Etheren#6893 can shut the bot down.')

@bot.command()
async def counter(ctx):
    global counterCheck
    counterCheck += 1
    await ctx.send('counter is now {0}'.format(counterCheck))
    
    
        
bot.run(TOKEN)
