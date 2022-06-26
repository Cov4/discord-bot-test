import discord
import random
import datetime
from discord.ext.commands import Bot
tk = "OTkwMjQwNjcwOTkwMTAyNTI4.GEasQk.NGjfRleIt-_GTMtoUIcEyIsWLdnwTQOsS_RqoQ"
client = discord.Client()

intents = discord.Intents.default()

client = Bot(command_prefix='!', intents = intents)

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
    print("bot is ready")
    print(client.user)
 


@client.command()
async def 명령어(ctx):
    await ctx.reply('!이름, !oplist, !opimfo')
    
@client.command()
async def sl1(ctx):
    embed = discord.Embed(title = "김동민의 남은 전역 일", description = None, color = "green")
    embed.add_field(name = "남은 일",value =":calender_spiral:"+client, inline= True)
    await ctx.reply(embed = embed)
@client.command()
async def sl2(ctx):
    await ctx.reply("한웅재의 남은 전역 일은" + v1)
@client.command()
async def sl3(ctx):
    await ctx.reply("홍의진의 남은 전역 일은" + v2)


@client.event
async def on_command_error(ctx, error):
    await ctx.send("명령어를 찾지 못했습니다.")

client.run(tk)