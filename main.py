from textwrap import TextWrapper
import requests
import json
import os
import sys
import textwrap
os.system("")

# input prompt
def input_prompt():
    print("\033[0;37;40mWhich type of data do you wanna see: (anime/manga)")
    input_prompt.data_type = input()

input_prompt()

# command parser
if input_prompt.data_type.lower() == "anime":
    print("Please type the Anime ID below:")
    id = input()
    url = requests.get("https://api.jikan.moe/v4/anime/"+id).json()
    loaded_json = json.dumps(url)
    if "error" in loaded_json:
        print("404 Not Found")
    else:
        episode_count_raw = url["data"]["episodes"]
        episode_count = episode_count_raw
        wrapper = textwrap.TextWrapper(width=70)
        synopsis = wrapper.wrap(text=url["data"]["synopsis"])
        print(" \033[0;31;40m" + "+++++++++++")
        print(" \033[0;32;40m" + url["data"]["title"])
        print(" \033[0;31;40m" + "+++++++++++")
        if episode_count_raw == None:
            episode_count = "???"
        print(" \033[0;36;40m" + str(episode_count) + " Episodes")
        print(" \033[0;36;40m" + "Duration: " + url["data"]["duration"])
        print(" \033[0;36;40m" + "Members: " + format(url["data"]["members"], "8,d"))
        print(" \033[0;36;40m" + "Favorites: " + format(url["data"]["favorites"], "8,d"))
        print(" \033[0;36;40m" + "Rank: " + str(url["data"]["rank"]))
        print(" \033[0;36;40m" + "Status: " + str(url["data"]["status"]))
        print(" \033[0;36;40m" + "Rating: " + "\033[1;31;40m" + str(url["data"]["rating"]))
        print(" \033[0;36;40m" + "Score: " + str(url["data"]["score"]))
        print(" \033[1;33;40m" + "Synopsis")
        print(" \033[1;33;40m" + "********")
        for element in synopsis:
            print(" \033[1;33;40m" + element)
elif input_prompt.data_type.lower() == "manga":
    print("Coming Soon..")
        
input('\033[1;32;40mPress any button to close the app')

# happy coding :)