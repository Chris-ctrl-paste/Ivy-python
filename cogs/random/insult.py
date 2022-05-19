import nextcord
from nextcord.ext import commands
import requests
import json
 
guilds = [647250925282656287]

class insult(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="insult", guild_ids = guilds, description="insults")
    async def insult(self, interaction):
        response_api = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')

        data = response_api.text
        parse_json = json.loads(data)
        info = parse_json['insult']
        await interaction.response.send_message(info)
        
       




def setup(client):
    client.add_cog(insult(client))