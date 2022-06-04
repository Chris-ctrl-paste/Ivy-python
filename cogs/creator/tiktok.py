import asyncio
from interactions import Channel
import nextcord
from nextcord.ext import commands
from tiktok_downloader import ttdownloader
import time

guilds = [647250925282656287]

class tiktok(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="tiktok", guild_ids = guilds, description="download tiktok video")
    async def tiktok(self, interaction, url):
        await interaction.response.defer()
        string = str(url)
        d=ttdownloader(string)
        d[0].download('./resources/tiktok/tiktokvideo.mp4')
        print("video downloading")
        await interaction.send(file=nextcord.File(r'.\resources\tiktok\tiktokvideo.mp4'))

def setup(client):
    client.add_cog(tiktok(client))
