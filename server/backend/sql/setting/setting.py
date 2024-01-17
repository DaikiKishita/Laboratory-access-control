from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

#環境ファイルから
env_path="../../envs/.env"
os.environ["PATH"]=env_path
host=os.environ["host"]
user=os.environ["user"]
password=os.environ["password"]
dbname=os.environ["db"]

#エンジン作成
Engine=create_engine(f"mysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4")

#モデルベースクラスを作成
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

