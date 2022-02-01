client = None

async def get_message(message):
  if message.author == client.user:
    return
  print(message)
  return