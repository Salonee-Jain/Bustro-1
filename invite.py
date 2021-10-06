import discord
import os
import requests
import json
from replit import db
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)




@client.event
async def on_member_join(member):
  guild = client.get_guild(890472628626812978)
  channel = guild.get_channel(894775731857539072)
  await channel.send(f'Welcome, {member.name}')
  await member.send(f"hello, {member.name}")