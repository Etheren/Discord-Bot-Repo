import discord
import sys
import os
from discord.ext import commands
from discord import opus
from discord.utils import get
from discord import FFmpegPCMAudio
import youtube_dl


class voiceCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None
        self.channel = None
        self.loop = False
        self.source = None

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
        self.source = FFmpegPCMAudio('song.mp3')
        self.player = self.voice.play(self.source)

    @commands.command()
    async def pause(self,ctx):
        self.voice.pause()

    @commands.command()
    async def volume(self,ctx, userInput : int):
        self.voice.volume = 100


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

    @commands.command(pass_context=True, brief="This will play a song 'play [url]'", aliases=['pl'])
    async def playyt(self, ctx, url: str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music end or use the 'stop' command")
            return
        await ctx.send("Getting everything ready, playing audio soon")
        print("Someone wants to play music let me get that ready for them...")
        self.voice = get(self.bot.voice_clients, guild=ctx.guild)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')
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
        self.source = FFmpegPCMAudio('song.mp3')
        self.player = self.voice.play(self.source)
        await ctx.send("If it's less than 8MB, this is the .mp3 file from audio extraction.")
        await ctx.send(file=discord.File('song.mp3'))


    @commands.command()
    async def leave(self,ctx):
        self.voice.stop()
        await self.voice.disconnect()

def setup(bot):
    bot.add_cog(voiceCommands(bot))