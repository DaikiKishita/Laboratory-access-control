#discordへ送信する際の処理を行うためにimport
import json
from urllib.request import Request, urlopen

#環境ファイル読み込み
import os
from dotenv import load_dotenv

#時間表記変更用
import math

"""
変数
"""

#送信するdiscordのwebhookurl
load_dotenv("envs/.env")
webhook=os.getenv("webhook")

status={
    "yellow":"面談中",
    "red":"学校外",
    "green":"研究室内",
    "silver":"学校内"
}

"""
関数
"""

def post_discord(message: str, webhook_url:str):
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

#変更前の色を保存
def get_before_color(Infos):
    return {Info.user_name:Info.color for Info in Infos}

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

#データ整理
def Get_datas(Infos):
    return [
        {
            'id':i.user_id,
            'name':i.user_name,
            'color':i.color,
            'status':status[i.color]
        } for i in Infos
    ]

def User_Timer(Infos):
    return {Info.user_name: Time() for Info in Infos}

"""
Class
"""
#入退室時間管理
class Time:
    def __init__(self):
        self.time=0
    
    def In(self,r):
        self.start=r
    
    def Out(self,r):
        self.time=r-self.start
        return self.time