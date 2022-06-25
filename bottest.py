import discord
import random
from discord.ext.commands import Bot
tk = "OTkwMjQwNjcwOTkwMTAyNTI4.GEasQk.NGjfRleIt-_GTMtoUIcEyIsWLdnwTQOsS_RqoQ"
client = discord.Client()

intents = discord.Intents.default()

client = Bot(command_prefix='!', intents = intents)

g = ['가위', '바위', '보']
randomset = random.choice(g)

@client.event
async def on_ready():
    print("bot is ready")
    print(client.user)
 
@client.command()
async def start(ctx):
    await ctx.reply('가위 바위 보를 시작 합니다.')
async def on_message(message):
    if randomset == '가위':
        if message.content == '가위':
            await message.channel.send("비겼습니다.")
        elif message.content == '바위':
            await message.channel.send("이겼습니다.")
        elif message.content == '보':
            await message.channel.send("졌습니다.")
    elif randomset == '바위':
        if message.content == '가위':
            await message.channel.send("졌습니다.")
        elif message.content == '바위':
            await message.channel.send("비겼습니다.")
        elif message.content == '보':
            await message.channel.send("이겼습니다.")
    elif randomset == '보':
        if message.content == '가위':
            await message.channel.send("이겼습니다.")
        elif message.content == '바위':
            await message.channel.send("졌습니다.")
        elif message.content == '보':
            await message.channel.send("비겼습니다.")

client.run(tk)