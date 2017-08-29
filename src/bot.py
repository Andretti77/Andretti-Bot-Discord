import discord 
from discord import Game
from discord.ext.commands import Bot
from urllib.request import urlopen 
import requests
from bs4 import BeautifulSoup
import asyncio as asyncio
import random
import Treasure

client = discord.Client()


@client.event
async def on_ready():
        print("Logged in")
        await client.change_presence(game=Game(name="Under Construction"))

        

async def hello(message):
       return await client.send_message(message.channel,"Hello!")



async def goodbye(message):
        return await client.send_message(message.channel,"Goodbye!")



async def youtube(message):
        results = []
        temp = message.content.replace("~youtube ","")
        search_terms = '+'.join(temp)
        url = "https://www.youtube.com/results?search_query=" + search_terms
        url_o = urlopen(url)
        html = url_o.read()
        s = BeautifulSoup(html, "lxml")
        for vids in s.find_all(attrs= {'class': 'yt-uix-tile-link'},limit = 1):
                results.append('https://www.youtube.com' + vids['href'])
        return await client.send_message(message.channel, results[0])

async def roll(message):
        dice = message.content.replace("~roll ", "")

        if dice == "d20":
               dice_roll = random.randint(1,21) 
        elif dice == "d6":
                dice_roll = random.randint(1,7)
        elif dice == "d10":
                dice_roll = random.randint(1,11)
        elif dice == "d4":
                dice_roll = random.randint(1,5)
        elif dice == "d100":
                dice_roll = random.randint(1,101)
        
        return await client.send_message(message.channel, dice_roll)


@client.event
async def on_message(message):

        if message.content.startswith("~hello"):
               await hello(message)
        elif message.content.startswith("~goodbye"):
                await goodbye(message)
        elif message.content.startswith("~youtube"):
                await youtube(message) 
        elif message.content.startswith("~roll"):
                await roll(message)
        elif message.content.startswith("~help"):
                help_message = []
                help_message.append("All commands start with ~.\n")
                help_message.append("~hello : A greeting.\n")
                help_message.append("~goodbye : A farewell.\n")                    
                help_message.append("~youtube: Searches YouTube and returns a link to the top result.")
                help_message.append("Format: ~youtube <Search Terms>\n")
                help_message.append("~roll : rolls a collection of dice. Dice include: d20, d6, d10, d4, d100")
                help_message.append("Format: ~roll <one dice listed above>\n")

                final_message = '\n'.join(help_message)
                await client.send_message(message.channel, final_message)


client.run(Treasure.KEY)
