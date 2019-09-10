import discord
from discord.ext import commands
from discord import opus
from discord.utils import get
from discord import FFmpegPCMAudio

class voiceCommands(commands.Cog):

    def __init__(self, bot, opus='opus'):
        self.bot = bot
        self.vc = None
        #discord.opus.load_opus

    @commands.command()
    async def joinChat(self,ctx):
        """Join The chat you stupid bot"""
        await ctx.send('Joining the chat kiddo')

    @commands.command()
    async def play(self,ctx):
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegPCMAudio('vuvuzela.mp3')
        player = voice.play(source)

def setup(bot):
    bot.add_cog(voiceCommands(bot))