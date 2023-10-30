from sql.ORM import Insert,Get,Update

#flaskをimport
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_cors import CORS

#modulesフォルダから
from modules.modules import Time,post_discord,make_time,get_before_color,Get_datas

#flaskappのクラス
app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config.from_object(__name__)
CORS(app)

before_color={}

@app.route('/')
def index():
    return render_template("index.html")

#baseページからGetの処理を受け取る
@app.route("/get_data",methods=["GET"])
def Get_Data():
    global before_color
    all_user=Get()
    responce=Get_datas(all_user)
    before_color=get_before_color(all_user)
    return jsonify(responce)

@app.route("/change_color",methods=["POST"])
def Change_Color():
    User_Info=request.get_json()
    name=User_Info['Name']
    color=User_Info['Color']
    if before_color[name] != color:
        Update(name,color)
        before_color[name]=color
    return render_template("index.html")

#ユーザーの新規追加処理
@app.route("/add_user",methods=["POST"])
def get_name():
    name=request.get_json()
    Insert(name["name"])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3140")