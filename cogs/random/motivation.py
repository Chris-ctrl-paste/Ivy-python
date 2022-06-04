import nextcord
from nextcord.ext import commands
import json
import random 
import requests


guilds = [647250925282656287]

class motivation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="motivation", guild_ids = guilds, description="Motivation Quote")
    async def motivation(self,interaction):
      
      
      
        with open("./resources/motivational.json") as f:
            content = json.loads(f.read())

        
        quote = random.choice(content['quotes'])
        wtf = quote['text']
        xd = quote['author']
        wtfxd = wtf + " - " + xd
        
    
        await interaction.response.send_message(wtfxd)
        
        
        f.close()
def setup(client):
    client.add_cog(motivation(client))