import discord
from discord.ext import commands


intents=discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True,message_content = True)
client=commands.Bot(command_prefix='-',intents=intents)
token=YourTokenAdress

@client.event
async def on_ready():
    print("ben hazirim!!")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content=message.content.lower()
    if message.content == 'Hi':
        await message.channel.send('Hello !')

client.run(token)
