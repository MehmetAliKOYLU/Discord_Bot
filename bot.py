import discord
from discord.ext import commands


intents=discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True,message_content = True)
client=commands.Bot(command_prefix='-',intents=intents)
token="MTAyNTg2MjUwNDkxMzU3MTk5MQ.GRcvPI.Wl46CNAVQi1BWZh7srY5MXxZFchIa3hK6js5pY"

@client.event
async def on_ready():
    print("ben hazirim!!")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content=message.content.lower()
    if message.content == 'qw':
        await message.channel.send('en iyisi')
    elif message.content=='sila':
        await message.channel.send('SILAA')
    elif message.content=='soner':
        await message.channel.send('ZORBA')
    elif message.content=='zort':
        await message.channel.send('Zattiri zort zort')
    elif message.content=='teto':
        await message.channel.send('Valo gelcen mi')
    elif message.content=='gorusuruz':
        await message.channel.send('gorusuruz canim')
    elif message.content=='bb':
        await message.channel.send('gorusuruz canim')
    elif message.content=='canim':
        await message.channel.send('soyle balim')
client.run(token)