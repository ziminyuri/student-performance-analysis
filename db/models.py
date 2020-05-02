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

    @staticmethod
    def all(session):
        try:
            list_name = session.query(Discipline.name).all()
            return list_name
        except Exception as e:
            session.rollback()
            print(str(e))

    @staticmethod
    def show_name(session):
        try:
            list_all = session.query(Discipline).all()
            ls_name = []
            for i in list_all:
                ls_name.append(i.name)

            return ls_name

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


class Work(Base):
    __tablename__ = 'work'
    id_work = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    id_group = Column(Integer, ForeignKey('group_table.id_group'), nullable=False, primary_key=True)
    group = relationship(Group, primaryjoin=id_group == Group.id_group, backref="parent_work_group")
    id_discipline = Column(Integer, ForeignKey('discipline.id_discipline'), nullable=False, primary_key=True)
    discipline = relationship(Discipline, primaryjoin=id_discipline == Discipline.id_discipline, backref="parent_work_group")

    @staticmethod
    def show_name(session, discipline, group_number):
        try:
            list_all = session.query(Work).all()
            ls = []
            ls.append("ФИО студента")
            for i in list_all:
                if i.discipline.name == discipline:
                    if i.group.number == group_number:
                        ls.append(i.name)
                        ls.append("Дата защиты")
            return ls

        except Exception as e:
            session.rollback()
            bd_error()


class Grade(Base):
    __tablename__ = 'grade'
    id_grade = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    id_work = Column(Integer, ForeignKey('work.id_work'), nullable=False, primary_key=True)
    work = relationship(Work, primaryjoin=id_work == Work.id_work, backref="parent_grade_work")
    id_student = Column(Integer, ForeignKey('student.id_student'), nullable=False, primary_key=True)
    student = relationship(Student, primaryjoin=id_student == Student.id_student, backref="parent_grade_student")

    @staticmethod
    def all(session, discipline, group_number):
        try:
            grade_all = session.query(Grade).join(Work).join(Discipline).join(Group).join(Student).filter(Discipline.name==discipline).filter(Group.number==group_number).order_by(Grade.id_student).all()
            student_all = session.query(Student).join(Group).filter(Group.number == group_number).order_by(Student.name).all()
            work_all = session.query(Work).join(Discipline).join(Group).filter(Discipline.name==discipline).filter(Group.number==group_number).order_by(Work.name).all()
            ls = []
            for i in student_all:
                row = []
                row.append(i.name)
                for j in work_all:
                    for k in grade_all:
                        if k.id_work == j.id_work and k.id_student == i.id_student:
                            row.append(k.value)
                            row.append(str(k.date))
                ls.append(row)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()