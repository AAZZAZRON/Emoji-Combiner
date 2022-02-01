import discord
import os
from keep_alive import keep_alive
import loadEmotes
import program


client = discord.Client()

# Runs when the bot starts up
@client.event
async def on_ready():
  global main_program, client
  program.client = client
  print(f"{client.user} initilized")


# Runs whenever there is a message
@client.event
async def on_message(message):
  if not program.client:
    if message.author != client.user:
      await message.channel.send("unintalized... please wait")
    return
  await program.get_message(message)


token = os.environ['TOKEN']
loadEmotes.start(client)
keep_alive()
client.run(token)
