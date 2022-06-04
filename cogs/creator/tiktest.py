import asyncio
from interactions import Channel
import nextcord
from nextcord.ext import commands
from tiktok_downloader import ttdownloader
import time

guilds = [647250925282656287]

class t(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="defer", guild_ids = guilds, description="download tiktok video")
    async def t(self, interaction):
      
        
        await interaction.response.defer()
        await asyncio.sleep(10)
        await interaction.send(file=nextcord.File(r'.\resources\tiktok\tiktokvideo.mp4'))

def setup(client):
    client.add_cog(t(client))
