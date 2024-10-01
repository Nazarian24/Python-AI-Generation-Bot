import discord
import getter
from discord.ext import commands, tasks

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):

    if message.content.split(" ")[0] == "!imagine":

        searchterm = message.content[9:]
        await message.channel.send("Generating image of " + searchterm + "...")

        getter.generate_image(searchterm)

        await message.channel.send(file=discord.File('result.jpg'))

client.run("Your discord Token Goes Here")