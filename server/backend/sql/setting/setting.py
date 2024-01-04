from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

#環境ファイルから
load_dotenv("envs/.env")
host="Write your mysql ip"
user="LACkun"
password="LACpass"
dbname="LAC"

#エンジン作成
Engine=create_engine(f"mysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4")

#モデルベースクラスを作成
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

