import discord
import datetime
token = "OTg5ODI4NzM4OTY5NjMyODY5.GRmQyO.QOPKpUmKdzndaSE0gQHvkl1QKId4Lc_ysWVQ9k"
client = discord.Client()

today = datetime.date.today()
targetday1 = datetime.date(2023,12,6)
targetday2 = datetime.date(2023,12,26)
value1 = targetday1 - today
value2 = targetday2 -today
v1 = str(value1)
v2 = str(value2)


@client.event
async def on_ready():
    print("Bot is ready")
    print(client.user)
    print("==========================")
    
@client.event
async def on_message(message):
    if message.content == "김동민의 전역까지 남은 일":
        await message.channel.send("김동민의 남은 전역 일은" + v1)
    elif message.content == "한웅재의 전역까지 남은 일":
        await message.channel.send("한웅재의 남은 전역 일은" + v1)
    elif message.content == "홍의진의 전역까지 남은 일":
        await message.channel.send("홍의진의 전역까지 남은 일은" + v2)
    elif message.content == "!명령어":
        await message.channel.send("(알고 싶은 병사의 이름) + 전역까지 남은 일")            
          
client.run(token)
