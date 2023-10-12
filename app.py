#model.pyからUserのclassを持ってくる
from model import User
from session import db_session

#envファイル読み込み用
import os
from dotenv import load_dotenv

#discordへ送信する際の処理を行うためにimport
import json
from urllib.request import Request, urlopen

#flaskをimport
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

#時間表記変更用
import math

#データベース
user=User()

#flaskappのクラス
app=Flask(__name__)

#送信するdiscordのwebhookurl
load_dotenv(".env")
webhook=os.getenv["webbook"]

#富樫研discordserverへ入退室の状況を送る為の関数
def post_discord(message: str, webhook_url=webhook):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
    }
    data = {"content": message}
    request = Request(
        webhook_url,
        data=json.dumps(data).encode(),
        headers=headers,
    )

    with urlopen(request) as res:
        assert res.getcode() == 204

#入退室時間管理
class Time:
    def __init__(self):
        self.time=0
    
    def In(self,r):
        self.start=r
    
    def Out(self,r):
        self.time=r-self.start
        return self.time

#時間表記を分かりやすくする為の関数
def make_time(r):
    string=""
    if r>=3600:
        hour=math.floor(r//3600)
        r=r%3600
        string+=f"{hour}時間"
    if r>=60:
        minute=math.floor(r//60)
        r=r%60
        string+=f"{minute}分"
    seconds=math.floor(r//1)
    string+=f"{seconds}秒"
    return string

@app.route("/",mthods=["GET","POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")