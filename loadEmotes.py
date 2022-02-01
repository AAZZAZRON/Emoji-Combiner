import json
from emoteVars import dates, emojis


client = None
rootUrl = "https://www.gstatic.com/android/keyboard/emojikitchen"


def start(c):
  client = c
  file = open("loaded.json")
  outputData = json.load(file)


  file.close()
  print("Emotes Loaded")



def reformat(emoji):
  return "-".join([x.lower() for x in emoji.split("-")])




  