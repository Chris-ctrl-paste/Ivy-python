from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import nextcord
import json
# from config import Token





client = commands.Bot(command_prefix='.')

guild_ids = [647250925282656287]


@client.event
async def on_ready():
    print(f'{client.user} has logged in.')
    

with open('./resources/config.json') as f:
    data = json.load(f)
    token = data["token"]
    # prefix = data["PREFIX"]
 


for folder in os.listdir(f'./cogs/.'):
    for filename in os.listdir(f'./cogs/{folder}/.'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{folder}.{filename[:-3]}')
            print({filename})



@client.command()
@commands.is_owner()
async def reload(ctx):
    try:
        for folder in os.listdir(f'./cogs/.'):
            for filename in os.listdir(f'./cogs/{folder}/.'):
                if filename.endswith('.py'):
                    client.reload_extension(f'cogs.{folder}.{filename[:-3]}')
                    print(f'"**{filename}**" Cog reloaded')
    except Exception as e:
        return print(e)





client.run(token)