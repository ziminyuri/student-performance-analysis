from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from transform.errors import bd_error

Base = declarative_base()


def get_user_password(session, login):
    user = session.query(Users).filter_by(login=login).first()

    try:
        return user

    except:
        return None


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)