import discord 
from discord.ext.commands import Bot


bot = Bot(command_prefix = "~")

@bot.event
async def on_read():
	print("Logged in")


@bot.command()
async def hello(*args):
	return await bot.say("Hello!")


@bot.command()
async def goodbye(*args):
	return await bot.say("Goodbye!")

bot.run("MzM3OTczMjM1NTAzMjAyMzA1.DFOptQ.lSWcXTTnDkY4Igoua0zJNXrX5YU")
