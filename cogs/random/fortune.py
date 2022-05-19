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
        # print(response_api.status_code)
        # print(response_api.json())
        
        
        data = response_api.text
        parse_json = json.loads(data)
        info = parse_json['fortune']
        await interaction.response.send_message(info)
        # key = parse_json['parameters']['key']['description']
        # print("\nDescription about the key:\n",key)
       




def setup(client):
    client.add_cog(fortune(client))