from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

#環境ファイルから
from backend.enviroments.enviroments import user,password,host,db

#エンジン作成
Engine=create_engine(f"mysql://{user}:{password}@{host}:3300/{db}?charset=utf8mb4")

#モデルベースクラスを作成
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

