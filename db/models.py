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


class Specialty(Base):
    __tablename__ = 'specialty'
    id_specialty = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    name = Column(String(255), nullable=False)

    @staticmethod
    def show_name(session):
        try:
            list_all = session.query(Specialty).all()
            ls_name = []
            for i in list_all:
                ls_name.append(i.name)

            return ls_name

        except Exception as e:
            session.rollback()
            print(str(e))


class Group(Base):
    __tablename__ = 'group_table'
    id_group = Column(Integer, primary_key=True)
    number = Column(String(100), nullable=False)
    id_specialty = Column(Integer, ForeignKey('specialty.id_specialty'), nullable=False, primary_key=True)
    specialty = relationship(Specialty, primaryjoin=id_specialty == Specialty.id_specialty, backref="p_specialty")

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.number, self.specialty.name)

    @staticmethod
    def show_name(session):
        try:
            list_all = session.query(Group).all()
            ls = []
            for i in list_all:
                ls.append(i.number)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def show_all(session):
        try:
            list = session.query(Group).all()
            ls = []
            for i in list:
                ls1 = []
                ls1.append(i.specialty.name)
                ls1.append(i.number)

                ls.append(ls1)

            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def add(session, number, specialty):
        try:
            s = session.query(Specialty).filter_by(name=specialty).first()
            id_specialty = s.id_specialty
            new_group = Group(number=number, id_specialty=id_specialty)
            session.add(new_group)
            session.flush()
        except Exception as e:
            bd_error()

    @staticmethod
    def update(session, old_number, number, specialty):
        try:
            s = session.query(Specialty).filter_by(name=specialty).first()
            id_specialty = s.id_specialty
            g = session.query(Group).filter_by(number=old_number)
            g.update({Group.number: number, Group.id_specialty: id_specialty})
            session.commit()

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def delete(session, number):
        try:
            s = session.query(Group).filter_by(number=number)
            s.delete()
            session.commit()

        except Exception as e:
            session.rollback()
            bd_error()


class Student(Base):
    __tablename__ = 'student'
    id_student = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    record_book = Column(Integer, nullable=False)
    id_group = Column(Integer, ForeignKey('group_table.id_group'), nullable=False, primary_key=True)
    group = relationship(Group, primaryjoin=id_group == Group.id_group, backref="parent_group")

    @staticmethod
    def all(session, group_number: str):
        try:
            student_list: list = session.query(Student).all()
            ls: list = []
            for i in student_list:
                if i.group.number == group_number:
                    ls1: list = []
                    ls1.append(i.name)
                    ls1.append(i.record_book)

                    ls.append(ls1)

            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def add(session, name, record_book, group_number):
        try:
            g = session.query(Group).filter_by(number=group_number).first()
            id_group = g.id_group
            new_student = Student(name=name, record_book=record_book, id_group=id_group)
            session.add(new_student)
            session.flush()

        except Exception as e:
            bd_error()

    @staticmethod
    def update(session, old_record_book, new_name, new_record_book):
        try:
            s = session.query(Student).filter_by(record_book=old_record_book)
            s.update({Student.record_book: new_record_book, Student.name: new_name})
            session.commit()

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def delete(session, record_book):
        try:
            s = session.query(Student).filter_by(record_book=record_book)
            s.delete()
            session.commit()

        except Exception as e:
            session.rollback()