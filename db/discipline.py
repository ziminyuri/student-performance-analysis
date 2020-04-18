from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Discipline(Base):
    __tablename__ = 'discipline'
    id_discipline = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def all(self, session):
        try:
            list_name = session.query(Discipline.name).all()
            return list_name
        except Exception as e:
            session.rollback()
            print(str(e))