import discord 
from discord import Game
from discord.ext.commands import Bot
from urllib.request import urlopen 
import requests
from bs4 import BeautifulSoup
import asyncio as asyncio

#bot = Bot(command_prefix = "~")
client = discord.Client()


@client.event
async def on_ready():
        print("Logged in")
        await client.change_presence(game=Game(name="Under Construction"))

        
#@bot.command()
async def hello(message):
       return await client.send_message(message.channel,"Hello!")


#@bot.command()
async def goodbye(message):
        return await client.send_message(message.channel,"Goodbye!")


#@bot.command()
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


@client.event
async def on_message(message):

        if message.content.startswith("~hello"):
               await hello(message)
        elif message.content.startswith("~goodbye"):
                await goodbye(message)
        elif message.content.startswith("~youtube"):
                await youtube(message) 




client.run("MzM3OTczMjM1NTAzMjAyMzA1.DFOptQ.lSWcXTTnDkY4Igoua0zJNXrX5YU")
