import nextcord
from nextcord.ext import commands

 
guilds = [647250925282656287]

class avatar(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="avatar", guild_ids = guilds, description="get avatar of @user")
    async def avatar(self, interaction, member : nextcord.Member = None):
        if member == None:
            member = self.author
        memberavatar = member.avatar.url
        
        await interaction.response.send_message(memberavatar)
        
        
        

def setup(client):
    client.add_cog(avatar(client))