import discord
import datetime
from discord.ext.commands import Bot
token = "OTg5ODI4NzM4OTY5NjMyODY5.GStyBd.4l5DuufwKVKeHhwi3_CjQ4qUSH8O1_3DoF3BY0"
client = discord.Client()

intents = discord.Intents.default()

client = Bot(command_prefix='~', intents=intents)

today = datetime.date.today()
targetday1 = datetime.date(2023,12,6)
targetday2 = datetime.date(2023,12,26)
value1 = targetday1 - today
value2 = targetday2 -today
v1 = str(value1)
v2 = str(value2)

sl1 = "김동민"
sl2 = "한웅재"
sl3 = "홍의진"

@client.event
async def on_ready():
    print("Bot is ready")
    print(client.user)
    print("==========================")
    
@client.command()
async def 명령어(ctx):
    await ctx.reply('!이름, !oplist, !opimfo')
    
@client.command()
async def sl1(ctx):
    await ctx.reply("김동민의 남은 전역 일은" + v1)
@client.command()
async def sl2(ctx):
    await ctx.reply("한웅재의 남은 전역 일은" + v1)
@client.command()
async def sl3(ctx):
    await ctx.reply("홍의진의 남은 전역 일은" + v2)

@client.event
async def on_message(message):
    if message.content == "김동민의 전역까지 남은 일":
        await message.channel.send("김동민의 남은 전역 일은" + v1)
    elif message.content == "한웅재의 전역까지 남은 일":
        await message.channel.send("한웅재의 남은 전역 일은" + v1)
    elif message.content == "홍의진의 전역까지 남은 일":
        await message.channel.send("홍의진의 전역까지 남은 일은" + v2)
        

client.run(token)
