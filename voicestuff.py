import discord
from discord.ext import commands
from discord import opus

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
    # grab the user who sent the command
        voice_channel=ctx.message.author.voice.channel
        # only play music if user is in a voice channel
        if voice_channel!= None:
            # create StreamPlayer
            self.vc= await self.bot.join_voice_channel(voice_channel)
            player = self.vc.create_ffmpeg_player('vuvuzela.mp3')
            player.start()
            while not player.is_done():
            # disconnect after the player has finished
                player.stop()
                await self.vc.disconnect()
        else:
            await ctx.say('User is not in a channel.')

def setup(bot):
    bot.add_cog(voiceCommands(bot))