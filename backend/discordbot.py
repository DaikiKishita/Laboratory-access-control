#discord運用の為のモジュール
import discord
from discord import app_commands
from discord.ext import tasks

#DB操作
from sql.ORM import GetUserFromColor 

#環境ファイル
import os
from dotenv import load_dotenv

#モジュール
from modules.modules import Get_datas

load_dotenv("backend/sql/envs/.envs")

TOKEN=os.getenv("TOKEN")

#設定
intents=discord.Intents.default()
intents.messages=True
intents.message_content=True
client =discord.Client(intents=intents)
bot = app_commands.CommandTree(client)
channel_sent = None

@client.event
async def on_ready():
    await bot.sync()

@bot.command(name="show",description="研究室に誰がいるかな")
async def show(interaction):
    post_word=""
    ctx=interaction
    users=Get_datas(GetUserFromColor("green"))
    if len(users)==0:
        post_word="現在研究室には誰もいません\nこれは富樫研の危機か？"
        await ctx.response.send_message(post_word)
    else:
        post_word="↓今現在研究室にいる人↓\n"
        for user in users:
            post_word+=f"・{user['name']}\n"
        await ctx.response.send_message(post_word)

@tasks.loop(seconds=60*60*24)
async def loop():
    print("アクセス対策として送っています")

loop.start()
client.run(TOKEN)