import re
import tools
from urllib.request import urlopen

rooturl = "https://www.gstatic.com/android/keyboard/emojikitchen"
client = None
years = ["20201001",  "20210218",  "20210521",  "20210831",  "20211115"]

async def get_message(message):
  if message.author == client.user:
    return
  msg = message.content

  matches = re.findall(":(.*):",msg) #checks anything thats wrapped with colons lol
  for lol in matches:
    lol = lol.replace(":","").split()
    if len(lol) == 2:
      a = lol[0]
      b = lol[1]
      if len(a) == 2:
        a = f"{('u{:X}'.format(ord(a[0]))).lower()}-{('u{:X}'.format(ord(a[1]))).lower()}"
      else:
        a=('u{:X}'.format(ord(a))).lower()
      if len(b) == 2:
        b = f"{('u{:X}'.format(ord(b[0]))).lower()}-{('u{:X}'.format(ord(b[1]))).lower()}"
      else:
        b=('u{:X}'.format(ord(b))).lower()  
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
#  - put like [prefix]help
#  - do somehting with slash commands to make emotes :)
