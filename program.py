import re
import tools
from urllib.request import urlopen
from replit import db

rooturl = "https://www.gstatic.com/android/keyboard/emojikitchen"
client = None
years = ["20201001",  "20210218",  "20210521",  "20210831",  "20211115"]
prefixes = db["prefix"]

async def get_message(message):
  if message.guild.id in prefixes:
    prefix = prefixes[message.guild.id]
  else:
    db["prefix"][message.guild.id] = "$"
    prefix = "$"

  if message.author == client.user:
    return
  msg = message.content
  if msg == f"{prefix}help" or msg == "<@!938091581351817296>":
    settings = { 
    "title" : "you asked for help?",
    "description" : f"""mash emotes together using the format: `:emote1 emote2:`
make sure there's a space between the emotes and that the emotes are unicode emojis (default emotes)
some may not exist

commands:
> - `{prefix}help`: this message
> - `{prefix}prefix`: set prefix I guess [default]
> - `/emojify [emote1] [emote2]`: slash command (COMING SOON)

emoji credits: emoji kitchen
    """,
    "color" : 0x3498db,
    "author" : message.author,
    "icon" : message.author.avatar_url,
    "thumbnail" : client.user.avatar_url,
    "footer" : "made by chelsea and aaron :^)"
    }
    await tools.send_embed(message.channel, settings)

  if f"{prefix}prefix" in msg or "<@!938091581351817296> prefix" in msg:
    param = ' '.join(msg.replace(f"{prefix}prefix","",1).replace("<@!938091581351817296> prefix","",1).split())
    db["prefix"][message.guild.id] = param
    prefixes[message.guild.id] = param
    await tools.send_message(message.channel,f"`{param}` is now the prefix.")
  matches = re.findall(":(.*):",msg) #checks anything thats wrapped with colons lol
  if len(matches) > 0:
    for match in matches:
      match = match.replace(":","").split()
      if len(match) == 2:
        a = match[0]
        b = match[1]
        a = '-'.join([f"{('u{:X}'.format(ord(iii))).lower()}" for iii in a])
        b = '-'.join([f"{('u{:X}'.format(ord(iii))).lower()}" for iii in b])
        urls = []
        for year in years:
          urls.extend([f"{rooturl}/{year}/{a}/{a}_{b}.png", f"{rooturl}/{year}/{b}/{b}_{a}.png"])
        for url in urls:
          try:
            meta = urlopen(url).info()
            if meta["content-type"] == "image/png":
              await tools.send_message(message.channel,url)
              break
          except:
            pass
        else:
          await tools.send_message(message.channel,"thing not found lol")

# todo
#  - resize
#  - maybe check if the emote is in the valid emoji list
#  - optimize by caching
#  - invite to servers 
#  - put like [prefix]help / [prefix]about / spawn message
#  - do somehting with slash commands to make emotes :)
#  - migrate things to functions
#  - work with custom emotes :eyes:
#  - perms for settting prefix
#  - unicode things that are more than 2 long
#  - emoji catch better
#  - do smth with this? https://raw.githubusercontent.com/xsalazar/emoji-kitchen/8b4e6608ce25e8891c1d6cb582d4d44055930877/src/Components/emojiData.json