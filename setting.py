
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

#環境ファイルから
load_dotenv(".env")
address=os.getenv["host"]
user=os.getenv["user"]
password=os.getenv["password"]
dbname=os.getenv["dbname"]

#エンジン作成
Engine=create_engine(f"mysql://{user}:{password}@{address}/{dbname}")

#モデルベースクラスを作成
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

