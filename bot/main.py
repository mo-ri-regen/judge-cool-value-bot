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

    # 指定のチャンネルのみコマンド実行できるようにする
    if message.channel.id != int(os.environ["CHANNEL_ID"]):
        return

    if message.content == '/cool':
        cool_value = random.randrange(6)
        
        text = f"{message.author.name}さんのクール度は"
        
        if message.content.startswith('/cool'):      
            if cool_value == 0:
                text += "☆☆☆☆☆\n"
            elif cool_value == 1:
                text += "★☆☆☆☆\n"
            elif cool_value == 2:
                text += "★★☆☆☆\n"
            elif cool_value == 3:
                text += "★★★☆☆\n"
            elif cool_value == 4:
                text += "★★★★☆\n"
            else:
                text += "★★★★★\n"

        text += "それでは今日もcoolな一日を！"
                
        await message.channel.send(text)
        
load_dotenv()

client.run(os.environ['TOKEN'])
