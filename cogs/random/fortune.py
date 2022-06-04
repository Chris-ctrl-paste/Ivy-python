import nextcord
from nextcord.ext import commands
import requests
import json
 
guilds = [647250925282656287]

class fortune(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="fortune", guild_ids = guilds, description="Fortune cookie")
    async def fortune(self, interaction):
        
        response_api = requests.get('http://yerkee.com/api/fortune')
        data = response_api.text
        parse_json = json.loads(data)
        info = parse_json['fortune']
        await interaction.response.send_message(info)
        
       




def setup(client):
    client.add_cog(fortune(client))