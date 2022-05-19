from interactions import Channel
import nextcord
from nextcord.ext import commands
import datetime
 
guilds = [647250925282656287]

class purge(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="purge", guild_ids = guilds, description="Clearing 1-100 messages")
    async def purge(self, interaction, limit):
        limit = int(limit)
      
        await interaction.channel.purge(limit= limit)
        await interaction.send("Messages has been deleted")
      
        
        

def setup(client):
    client.add_cog(purge(client))