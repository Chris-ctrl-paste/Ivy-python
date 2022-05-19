import nextcord
from nextcord.ext import commands




guilds = [647250925282656287]

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="ping", guild_ids = guilds, description="pinging Ivy")
    async def ping(self, interaction):
        await interaction.response.send_message(f"ping: {round (self.client.latency * 1000)}ms")
        
        
        

def setup(client):
    client.add_cog(ping(client))