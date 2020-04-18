from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id_student = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    record_book = Column(Integer, nullable=False)

    def all(self, session):
        try:
            list_name = session.query(Student).all()
            return list_name
        except Exception as e:
            session.rollback()
            print(str(e))

    def add(self, session, name, record_book):
        new = Student(name=name, record_book=record_book)
        session.add(new)
        session.flush()

    def update(self, session, old_record_book, new_name, new_record_book):
        s = session.query(Student).filter_by(record_book=old_record_book)
        s.update({Student.name: new_name, Student.record_book: new_record_book })
        session.commit()

    def delete(self, session, record_book):
        try:
            s = session.query(Student).filter_by(record_book=record_book)
            s.delete()
            session.commit()

        except Exception as e:
            session.rollback()