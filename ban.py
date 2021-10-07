import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from better_profanity import profanity 
from discord.ext import commands

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

keep_alive()

my_secret = os.environ['botkey']

clients.run(my_secret)