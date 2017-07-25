import discord 
from discord.ext.commands import Bot
from urllib.request import urlopen 
import requests
from bs4 import BeautifulSoup
import asyncio as asyncio

bot = Bot(command_prefix = "~")
#client = discord.Client()


@bot.event
async def on_ready():
        print("Logged in")
        #client.change_presence(game=discord.Game(name="WIP"))
        
@bot.command()
async def hello(*args):
        return await bot.say("Hello!")


@bot.command()
async def goodbye(*args):
        return await bot.say("Goodbye!")

@bot.command()
async def youtube(*args):
        results = []
        search_terms = '+'.join(args)
        url = "https://www.youtube.com/results?search_query=" + search_terms
        url_o = urlopen(url)
        html = url_o.read()
        s = BeautifulSoup(html, "lxml")
        for vids in s.find_all(attrs= {'class': 'yt-uix-tile-link'},limit = 1):
                results.append('https://www.youtube.com' + vids['href'])
                
       
        return await bot.say(results[0])


bot.run("MzM3OTczMjM1NTAzMjAyMzA1.DFOptQ.lSWcXTTnDkY4Igoua0zJNXrX5YU")
