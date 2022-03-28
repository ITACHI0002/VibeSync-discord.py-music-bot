import discord
from discord.ext import commands
import music

from keepalive import keepalive

import json
import os


cogs = [music]



if os.path.exists(os.getcwd() + "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")
    await client.change_presence(activity=discord.Game(name="!help"))

for i in range(len(cogs)):
    cogs[i].setup(client)
   
   
   
keepalive()
client.run("YOUR_TOKEN_HERE")

