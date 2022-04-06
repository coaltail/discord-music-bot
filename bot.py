import discord
from discord.ext import commands
import requests
from main import *
from dotenv import load_dotenv
import os
load_dotenv()
token = os.environ.get("TOKEN")

client = commands.Bot(command_prefix='#')


@client.event
async def on_ready():
    print('Hello {0.user}'.format(client))


@client.command()
async def hello(ctx):
    await ctx.send("Hello bingle!")


@client.command()
async def ginger(ctx):
    await ctx.send(jsonData)

client.run(token)
