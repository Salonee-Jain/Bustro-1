import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from better_profanity import profanity 
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))
  

@client.event
async def on_member_join(member):
  guild = client.get_guild(os.environ['guild'])
  channel = guild.get_channel(os.environ['channel'])
  await channel.send(f'Welcome, {member.name}')
  await member.send(f"hello, {member.name}")

clients = commands.Bot(command_prefix='.')

@clients.command()
async def kick(ctx, member: discord.Member,*, reason=None):
  await member.kick(reason=reason)

@clients.command()

async def ban(ctx, member: discord.Member,*, reason=None):
  print("banning")
  await member.ban(reason=reason)
  print("banned")

@clients.command()
async def unban(ctx,*, member):
  banned_users=await ctx.guild.bans()
  print(ctx.guild.bans())

  





def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quotes = json_data[0]['q'] + "\n-"+json_data[0]['a']
  return quotes
 
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("/hello"):
    greet=["Hello","Hola","Bonjour","Ciao","Namaste"]
    await message.channel.send(str(greet[random.randint(0,5)])+" "+str(message.author))
  
  if message.content.startswith("/Inspire"):
    await message.channel.send(get_quote())

  cuss= '''
  fuck
  bitch
  cunt
  '''
    
  # do censoring 
  
  
  

  cuss_words = cuss.strip().split("\n")
  for i in cuss_words:
    if (i.strip() in message.content.lower()):
      await message.delete()
        
      await message.channel.send("Do not use restricted words")
      break
  

              

  


my_secret = os.environ['botkey']


keep_alive()
client.run(my_secret)




