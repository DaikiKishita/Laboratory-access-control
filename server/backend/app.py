from backend.sql.ORM import Insert,Get,Update

#flaskをimport
from flask import Flask, render_template, request, redirect, url_for,jsonify

#modulesフォルダから
from backend.modules.modules import post_discord,make_time,get_before_color,Get_datas,User_Timer,webhook,Time

import time

def create_app():
    #flaskappのクラス
    app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')

    #起動時の初期処理
    all_user=Get()
    Users_Timer=User_Timer(all_user)#ユーザーごとの時間管理用
    before_color=get_before_color(all_user)#現在の色の保持

    #Vueアプリケーションへの接続
    @app.route('/')
    def index():
        return render_template("index.html")

    #baseページからGetの処理を受け取る
    @app.route("/get_data",methods=["GET"])
    def Get_Data():
        all_user=Get()#データベースに格納されているユーザーの情報
        responce=Get_datas(all_user)#返り値
        return jsonify(responce)

    @app.route("/change_color",methods=["POST"])
    def Change_Color():
        User_Info=request.get_json()#postされたデータを受け取る
        name=User_Info['Name']#変数
        color=User_Info['Color']#変数
        
        if before_color[name] != color:#状態遷移が起こったかの判定
            Update(name,color)
            
            t=time.time()#時間取得
            if color=="green":#状態が緑になった時に時間を保存
                Users_Timer[name].In(t)
                post_discord(f"{name}が入室しました",webhook)
            elif before_color[name]=="green":#以前の色が緑の時、退出と判断する
                times=Users_Timer[name].Out(t)
                post_discord(f"{name}が退出しました\n滞在時間: {make_time(times)}",webhook)
            
            before_color[name]=color#現在の色の変更
        return render_template("index.html")

    #ユーザーの新規追加処理
    @app.route("/add_user",methods=["POST"])
    def get_name():
        name=request.get_json()
        Insert(name["name"])
        before_color[name["name"]]="royalblue"
        Users_Timer[name["name"]]=Time()
        return redirect(url_for("index"))
    
    return app

app=create_app()