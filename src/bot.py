import discord 
from discord.ext.commands import Bot

import requests

bot = Bot(command_prefix = "~")






@bot.event
async def on_ready():
	print("Logged in")


@bot.command()
async def hello(*args):
	return await bot.say("Hello!")


@bot.command()
async def goodbye(*args):
	return await bot.say("Goodbye!")


#@bot.command()
#async def youtube(url)
#	if url.contents.starts


bot.run("MzM3OTczMjM1NTAzMjAyMzA1.DFOptQ.lSWcXTTnDkY4Igoua0zJNXrX5YU")
