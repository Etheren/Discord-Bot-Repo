import discord, discordtoken , random
from discord.ext import commands

TOKEN = discordtoken.TOKEN
#You're not getting the bot token THIS easily. Ive already seen one server get
#Destroyed by it being left here.

description = '''AmiBot'''
bot = commands.Bot(command_prefix=';', description=description)
bot.load_extension('degencommands')
bot.load_extension('mapsimulator')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")

@bot.command()
async def add(ctx, left : int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)	
	
@bot.command()
async def google(ctx):
	"""Google Something?"""
	await ctx.send("www.google.co.uk")
	
@bot.command()
async def test(ctx):
	await ctx.send("@everyone fuk da popo")
	
@bot.command()
async def randomroll(ctx, left : int, right : int):
	"""Roll a random number between 1 and 10"""
	randomoutput = random.randint(left, right)
	await ctx.send(randomoutput)
	
@bot.command()
async def multimessage(ctx):
	"""output a multiline message"""
	await ctx.send("this is a test to see if multi messages can be sent")
	await ctx.send("if not, whoops")
	
		
bot.run(TOKEN)
