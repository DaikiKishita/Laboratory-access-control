from backend.sql.session.session import db_session
from backend.sql.models.User import User

#データベースへ情報を格納する
def Insert(name:str):
    new_user=User(user_name=name,color="royalblue")
    db_session.add(new_user)
    db_session.commit()

#データベースから情報を持ってくる
def Get():
    all_user = db_session.query(User).all()
    return all_user

#update処理
def Update(name:str,Color:str):
    query = db_session.query(User)
    user_update=query.filter(User.user_name == name).first()
    user_update.color=Color
    db_session.commit()

    """
    ↓discordbot専用関数↓
    """

def GetUserFromColor(color:str):
    users=db_session.query(User).filter(User.color==color).all()
    return users