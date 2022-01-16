"""
Outliner Discord Bot
Date: January 16, 2022
Developers: Aditya Singh Attri, Belal Kourkmas, Christie Tsang, 
            Sepehr Zohoori Rad
"""

import discord
import os
from scraper import generate_content
from ai_answers import ask
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  # await message.channel.send('We have logged in as {0.user}'.format(client))
  print('We have logged in as {0.user}'.format(client))


@client.event
#     message is received from user
async def on_message(message):
  if message.author == client.user:
      return

  if message.content.startswith('$upload'):
      links = message.content.replace('$upload\n', '')
      with open('links.txt', 'w') as file_object:
          file_object.write(links)
      await message.channel.send("Links uploaded successfully!")

  if message.content.startswith('$init'):
      try:
          generate_content()
      except Exception:
          await message.channel.send("Initialization failed!")
      else:
          await message.channel.send("Content generated successfully!")

  if message.content.startswith('$ask'):
      question = message.content.replace("$ask ", "")
      id = message.author.id
      await message.channel.send(f'<@{id}>\n' + ask(question))

  if message.content.startswith('$help'):
      await message.channel.send("God helps those who help themselves")


keep_alive()
client.run(os.environ['TOKEN'])
