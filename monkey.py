import re
import tools
from replit import db
import emoji
from urllib.request import urlopen
import unicodedata

rooturl = "https://www.gstatic.com/android/keyboard/emojikitchen"
client = None
knownDates = []

async def get_message(message):
  if message.author == client.user:
    return
  msg = message.content

  # emotes
  matches = re.findall(":(.*):", "".join(msg.split())) #checks anything thats not whitespace
  print(matches)
  for lol in matches:
    if len(lol) >= 2:
      lol = lol.replace(":","")
      #print((":"+'_'.join(unicodedata.name(lol[0]).lower().split())+":") in emoji.UNICODE_EMOJI)
      #print(lol[1])#, emoji.UNICODE_EMOJI)
      #print(emoji.UNICODE_EMOJI)
      #if lol[0] in emoji.UNICODE_EMOJI and lol[1] in emoji.UNICODE_EMOJI:
      if True:
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
          #print(a,b)
          print(a,b)
          urls = []
          for year in knownDates:  # initialized from json on startup
            urls.extend([f"{rooturl}/{year}/{a}/{a}_{b}.png", f"{rooturl}/{year}/{a}/{a}_{b}.png", f"{rooturl}/{year}/{b}/{b}_{a}.png", f"{rooturl}/{year}/{b}/{a}_{b}.png"])
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


  # for buffer in matches:
    #if buffer in db["emotes"]:
    #  await tools.send_message(message.channel, db["emotes"][buffer] + "?size=44")

  #return


def reformat(uni):
  return "u" + "-".join([x.lower() for x in uni.split("-")])

