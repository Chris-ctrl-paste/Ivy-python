from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import nextcord
import json
from argparse import ArgumentParser
from urllib.parse import parse_qsl, urlparse
import requests
import tweepy

client = commands.Bot(command_prefix='.')

guild_ids = [647250925282656287]


@client.event
async def on_ready():
    print(f'{client.user} has logged in.')
    

with open('./resources/config.json') as f:
    data = json.load(f)
    token = data["token"]
    CONSUMER_KEY = data["CONSUMER_KEY"]
    CONSUMER_SECRET = data["CONSUMER_SECRET"]
    ACCESS_TOKEN = data["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = data["ACCESS_TOKEN_SECRET"]

    
 


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





client.run(token)