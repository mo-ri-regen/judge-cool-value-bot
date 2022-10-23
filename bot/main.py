import discord

import os
from dotenv import load_dotenv

import judge_cool_bot
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
    
    # 強制終了する
    if message.content == '/logout':
        print("ログアウトしました")
        await client.close()
        return
        
    if message.content == '/cool':
        cool_value = judge_cool_bot.generate_random_number()
 
        text = judge_cool_bot.create_text(message.author.name, cool_value)
                
        await message.channel.send(text)

load_dotenv()

client.run(os.environ['TOKEN'])
