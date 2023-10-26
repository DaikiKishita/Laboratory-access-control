from sql.ORM import Insert

#flaskをimport
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_cors import CORS

#modulesフォルダから
from modules.modules import Time,post_discord,make_time

#flaskappのクラス
app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config.from_object(__name__)
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route("/new_user",methods=["POST"])
def get_name():
    name=request.get_json()
    print(type(name))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="3140")