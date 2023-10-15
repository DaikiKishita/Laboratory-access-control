from sqlalchemy.orm import sessionmaker,scoped_session
from sql.setting.setting import Engine

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=Engine
    )
)