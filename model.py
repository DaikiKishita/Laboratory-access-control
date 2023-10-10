#settingファイルからBaseとEngineをimport
from setting import Base,Engine
from session import db_session

#
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String,Datetime

class User(Base):
    __tablename__="User"
    user_id=Column("user_id",Integer,primary_key=True,autoincrement=True)
    user_name=Column("user_name",String(100),nullable=False)
    color=Column("color",String(10),nullable=False)


Base.query  = db_session.query_property()
Base.metadata.create_all(Engine)

