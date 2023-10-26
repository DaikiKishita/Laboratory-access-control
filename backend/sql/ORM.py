from sql.session.session import db_session
from sql.models.User import User

def Insert(name:str):
    new_user=User(user_name=name,color="silver")
    db_session.add(new_user)
    db_session.commit()
