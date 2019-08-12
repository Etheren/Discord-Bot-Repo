import discord, discordtoken
from discord.ext import commands

TOKEN = discordtoken.TOKEN
#You're not getting the bot token THIS easily. Ive already seen one server get
#Destroyed by it being left here.

description = '''Etherbot'''
bot = commands.Bot(command_prefix=';', description=description)

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
		
bot.run(TOKEN)
