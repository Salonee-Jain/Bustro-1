import discord
import os
import requests
import json


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quotes = json_data[0]['q'] + "\n-"+json_data[0]['a']
  return quotes
 


get_quote()
@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("/hello"):
    await message.channel.send("Hello!")
  
  if message.content.startswith("/Inspire"):
    await message.channel.send(get_quote())


  cuss_words = ["fuck", "asshole", "bastard", "cunt", "fucker", "bitch"]

  for i in cuss_words:
    if (i in message.content.lower()):
      await message.delete()
      
      await message.channel.send("{0} to you {1}".format(i,message.author))
      break

  


my_secret = os.environ['botkey']
client.run(my_secret)




