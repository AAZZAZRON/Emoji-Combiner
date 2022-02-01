import re
import tools
from replit import db


client = None

async def get_message(message):
  if message.author == client.user:
    return
  a = message.content

  # emotes
  matches = re.findall(":([\w]{2,32}):", a)
  for buffer in matches:
    if buffer in db["emotes"]:
      await tools.send_message(message.channel, db["emotes"][buffer] + "?size=44")

  return