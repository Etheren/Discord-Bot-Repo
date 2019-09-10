import discord
import sys
from discord.ext import commands
from discord import opus
from discord.utils import get
from discord import FFmpegPCMAudio
import youtube_dl

class voiceCommands(commands.Cog):

    def __init__(self, bot, opus='opus'):
        self.bot = bot
        self.voice = None
        self.player = None
        self.channel = None
        self.loop = False
        #discord.opus.load_opus

    @commands.command()
    async def joinChat(self,ctx):
        """Join The chat you stupid bot"""
        await ctx.send('Joining the chat kiddo')

    @commands.command()
    async def play(self,ctx):
        self.channel = ctx.message.author.voice.channel
        if not self.channel:
            await ctx.send("You are not connected to a voice channel")
            return
        self.voice = get(self.bot.voice_clients, guild=ctx.guild)
        if self.voice and self.voice.is_connected():
            await self.voice.move_to(self.channel)
        else:
            self.voice = await self.channel.connect()
        source = FFmpegPCMAudio('vuvuzela.mp3')
        self.player = self.voice.play(source)

    @commands.command()
    async def pause(self,ctx):
        self.voice.pause()

    @commands.command()
    async def resume(self,ctx):
        self.voice.resume()
    
    @commands.command()
    async def stop(self,ctx):
        self.voice.stop()

    @commands.command()
    async def join(self,ctx):
        self.channel = ctx.message.author.voice.channel
        if not self.channel:
            await ctx.send("You are not connected to a voice channel")
            return
        self.voice = get(self.bot.voice_clients, guild=ctx.guild)
        if self.voice and self.voice.is_connected():
            await self.voice.move_to(self.channel)
        else:
            self.voice = await self.channel.connect()
            await ctx.send("Joining Channel {0}".format(self.channel))

    @commands.command()
    async def leave(self,ctx):
        self.voice.stop()
        await self.voice.disconnect()

def setup(bot):
    bot.add_cog(voiceCommands(bot))