from sqlalchemy.orm import sessionmaker
from setting import Engine
SessionClass = sessionmaker(Engine)  # セッションを作るクラスを作成
session = SessionClass()