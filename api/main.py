import discord
import random

import os
from dotenv import load_dotenv

# 接続に必要なオブジェクトを生成

client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
# 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
# メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == '/cool':
        cool_value = random.randrange(6)
        
        text = "あなたのクール度は"
        
        if message.content.startswith('/cool'):      
            if cool_value == 0:
                text += "☆☆☆☆☆"
                await message.channel.send(text)
            elif cool_value == 1:
                text += "★☆☆☆☆"
                await message.channel.send(text)
            elif cool_value == 2:
                text += "★★☆☆☆"
                await message.channel.send("★★☆☆☆")
            elif cool_value == 3:
                text += "★★★☆☆"
                await message.channel.send("★★★☆☆")
            elif cool_value == 4:
                text += "★★★★☆"
                await message.channel.send("★★★★☆")                                
            else:
                text += "★★★★★"
                await message.channel.send(text)

load_dotenv()

client.run(os.environ['TOKEN'])
