import json, requests


client = None
rootUrl = "https://www.gstatic.com/android/keyboard/emojikitchen"
outputData = {}

def start(c):
  global client, outputData, rootUrl
  client = c

  # ----- get JSON -----
  with open("loaded.json") as f:
    outputData = json.load(f)
  with open("knownDates.json") as f:
    knownDates = json.load(f)
  with open("knownEmojis.json") as f:
    knownEmojis = json.load(f)
  

  # ----- search for new emotes -----
  for currDate in knownDates:
    for left in knownEmojis:
      if left["name"] == "":
        continue
      leftUni = reformat(left["unicode"])
      for right in knownEmojis:
        if right["name"] == "" or left == right:
          continue
        rightUni = reformat(right["unicode"])
        
        emoteName = left["name"] + right["name"]
        emoteUrl = f"{rootUrl}/{currDate}/{leftUni}/{leftUni}_{rightUni}.png"

        # if emote not already found
        if emoteName not in outputData:
          
          resp = requests.get(url=emoteUrl, params={'responseType': 'stream', 'timeout': 5000})
          if resp.status_code == 200:
            outputData[emoteName] = emoteUrl
        
  
  # ----- write to file -----
  json_object = json.dumps(knownEmojis, indent=2)
  with open("knownEmojis.json", "w") as f:
    f.write(json_object)
  
  json_object = json.dumps(outputData, indent=2)
  with open("loaded.json", "w") as f:
    f.write(json_object)
  
  # ----- done -----
  print("Emotes Loaded")


def reformat(uni):
  return "u" + "-".join([x.lower() for x in uni.split("-")])




  