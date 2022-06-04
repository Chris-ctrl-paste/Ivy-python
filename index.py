from nextcord import Interaction, SlashOption, ChannelType, Activity, ActivityType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import nextcord
import json
from argparse import ArgumentParser
from urllib.parse import parse_qsl, urlparse
import requests
import tweepy
intents = nextcord.Intents.all()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='.', intents=intents)

guild_ids = [647250925282656287]


@client.event
async def on_ready():
    print(f'{client.user} has logged in.')
    await client.change_presence(activity=nextcord.Game(name="Trying my best"))

with open('./resources/config.json') as f:
    data = json.load(f)
    token = data["token"]
    CONSUMER_KEY = data["CONSUMER_KEY"]
    CONSUMER_SECRET = data["CONSUMER_SECRET"]
    ACCESS_TOKEN = data["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = data["ACCESS_TOKEN_SECRET"]

    
 
@client.event
async def on_presence_update(before, after):
   
    activity_type = None
    streaming_role = after.guild.get_role(772062410789617696)
    try:
        activity_type = after.activity.type
    except:
        pass

    if (activity_type is not nextcord.ActivityType.playing):
        if streaming_role in after.roles:
            print(f"{after.display_name} has stopped streaming")
            await after.remove_roles(streaming_role)
    else:
        if streaming_role not in after.roles:
            print(f"{after.display_name} has started streaming")
            await after.add_roles(streaming_role)

        
 
 
 
 
 
 
 
 
 
 
 
 
 
 


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




def main():
    twitter_auth_keys = {
        "consumer_key"        :  CONSUMER_KEY,
        "consumer_secret"     :  CONSUMER_SECRET,
        "access_token"        :  ACCESS_TOKEN,
        "access_token_secret" :  ACCESS_TOKEN_SECRET
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
 
    tweet = "Test 2 tweet python"
    status = api.update_status(status=tweet)
 
# if __name__ == "__main__":
#     main()


    
    
    
    # print("Is this doing something?")
    # activity_type = None
    # streaming_role = after.guild.get_role(772062410789617696)
    # try:
    #     activity_type = after.activity.type
    # except:
    #     pass

    # if not (activity_type is nextcord.ActivityType.playing):
    #         # User is doing something other than streaming
    #     if streaming_role in after.roles:
    #         print(f"{after.display_name} has stopped streaming")
    #         await after.remove_roles(streaming_role)
    # else:
    #     if streaming_role not in after.roles:
    #             # If they don't have the role, give it to them
    #             # If they have it, we already know they're streaming so we don't need to do anything
    #         print(f"{after.display_name} has started streaming")
    #         await after.add_roles(streaming_role)


client.run(token)