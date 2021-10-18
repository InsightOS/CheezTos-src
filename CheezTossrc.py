import discord
from discord.ext import commands
import os
from Webserver import keep_alive
import random
from discord_components import *
from discord_components import Button, ButtonStyle,DiscordComponents
import discord_buttons_plugin
from discord_buttons_plugin import *
from discord.ext.commands import *
from discord import *


#command_prefix (very important)
client = commands.Bot(command_prefix='~', case_insensitive=True)
buttons = ButtonsClient(client)

#Bot on_ready function down here 
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="~help"))
  print(f'{client.user} is ready!')
  DiscordComponents(client)
  
#Questions, The main part
q1 = 'Did Alan Turing Crack The Enigma Code?'
#Only 1 question shown here since i do not want others to copy questions. This code is source code only for people who want to make a quiz bot without an API
 
#Button functions and quiz function
@client.command()
async def quiz(ctx):
  #random number chooser: (import random for this)
  random_num = random.randint(1, 1)'''(the number to which you want to randomize until)'''
  if random_num == 1:
    embed = discord.Embed(
      title = q1,
      description = "Click on True/False depending on the answer",
      colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    await buttons.send(  
    content = "Click On The Options!",
    channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            style = ButtonType().Primary,
            label = "True",
            custom_id = "true1"
          ),
          Button(
            style = ButtonType().Danger,
            label = "False",
            custom_id = "false1"
          )


      
      ])
    ])

@buttons.click
async def true1(ctx):
  ctx.reply("Correct Answer!")

@buttons.click
async def false1(ctx):
  ctx.reply("Wrong Answer!")  


#POLL FUNCTION:
@client.command()
async def poll(ctx, *, message):
  emb = discord.Embed(title = f"POLL: {message}", description = 'May The Majority Decide!')
  await ctx.channel.send(embed=emb)
 
keep_alive() 
client.run("PUT YOUR TOKEN HERE")